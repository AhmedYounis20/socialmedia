from datetime import date
from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
class Account(User):
    birth=models.DateField(null=True,blank=True)
    address=models.TextField(null=True,blank=True)
    class Meta:
        verbose_name='Account'
    def __str__(self):
        return self.username
class Post(models.Model):
    text=models.TextField()

    created_at=models.DateTimeField(auto_now_add=True)
    published_at=models.DateTimeField(null=True,blank=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    owner=models.ForeignKey(Account,on_delete=models.CASCADE)
   
    def publish(self):
        self.published_at= timezone.now()

    def __str__(self):
        return self.Text
    

class Group(models.Model):
    name=models.CharField(max_length=150)
    description = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    published_at=models.DateTimeField(null=True,blank=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    owner=models.ForeignKey(Account,on_delete=models.CASCADE)
    
    members=models.ManyToManyField(Account,through='Membership',related_name='Groups')
    posts=models.ForeignKey(Post,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
class Membership(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateTimeField()

    def accept(self):
        self.date_joined=timezone.now()


