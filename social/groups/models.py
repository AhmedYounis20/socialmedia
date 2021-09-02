from django.db import models
from django.utils import timezone
# Create your models here.
from django.urls import reverse
from django.contrib.auth import get_user_model
User=get_user_model()
from django import template
register=template.Library()

class Group(models.Model):
    name=models.CharField(max_length=150)
    description = models.TextField()
    slug=models.SlugField(allow_unicode=True,unique=True,default=None)
    created_at=models.DateTimeField(auto_now_add=True)
    published_at=models.DateTimeField(null=True,blank=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    owner=models.ForeignKey('accounts.Account',on_delete=models.CASCADE)
    
    members=models.ManyToManyField('accounts.Account',blank=True,through='groups.Membership',related_name='members')
    posts=models.ForeignKey('posts.Post',blank=True,null=True,on_delete=models.SET_NULL)
    def save(self,*args,**kwargs):
        self.slug=self.name
        self.updated_at=timezone.now()
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('groups:single',kwargs={'slug':self.slug})
    def __str__(self):
        return self.name

class Membership(models.Model):
    account = models.ForeignKey('accounts.Account', on_delete=models.CASCADE)
    group = models.ForeignKey('groups.Group', on_delete=models.CASCADE)
    date_joined = models.DateTimeField()

    def accept(self):
        self.date_joined=timezone.now()
