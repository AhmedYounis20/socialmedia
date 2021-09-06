from typing import Text
from django.db.models.fields import DateTimeField, TextField
from django.db.models.fields.related import ForeignKey, OneToOneField
from groups.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    text=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    published_at=models.DateTimeField(null=True,blank=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    owner=models.ForeignKey('accounts.Account',on_delete=models.CASCADE)
    group=models.ForeignKey('groups.Group',related_name='posts',null=True,blank=True,on_delete=models.CASCADE)
    def publish(self):
        self.published_at= timezone.now()

    def __str__(self):
        return self.text
    def get_absolute_url(self):
        return reverse('posts:PostDetail',kwargs={'username': self.owner.username,'pk':self.pk})
        

class Comment(models.Model):
    text=models.TextField()
    owner=models.ForeignKey('accounts.Account',on_delete=models.CASCADE)
    published_at=models.DateTimeField(null=True,blank=True)
    post=models.ForeignKey('posts.Post',on_delete=models.CASCADE,related_name='comments',null=True,blank=True)
    def __str__(self):
        return self.text
    def publish(self):
        self.published_at= timezone.now()
