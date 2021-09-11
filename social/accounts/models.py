from datetime import date
from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from django.contrib.auth import models as m 



class Account(models.Model):
    first_Name=models.CharField(max_length=150,blank=True ,null=True)
    last_Name=models.CharField(max_length=150,blank=True ,null=True)
    username=models.CharField(max_length=150,blank=True ,null=True)
    user=models.OneToOneField(m.User,on_delete=models.CASCADE,null=True,related_name='cas')
    birth=models.DateField(null=True,blank=True,)
    Email_address=models.EmailField(null=True,blank=True)
    address=models.TextField(null=True,blank=True)
    groups=models.ManyToManyField('groups.Group',through='groups.Membership',related_name='groups')
    friend_to=models.ManyToManyField('accounts.Account',blank=True,related_name='friends')
    about=models.TextField(null=True , blank=True)
    def save(self,*args,**kwargs):
        if self.username==None:
            self.username=self.user.username
        if self.last_Name==None:
            self.last_Name=self.user.last_name
        if self.first_Name==None:
            self.first_Name=self.user.first_name
        if self.Email_address==None:
            self.Email_address= self.user.email
        return super().save(*args,**kwargs)

    class Meta:
        verbose_name='Account'
    def __str__(self):
        return '@{}'.format(self.username)
    def get_absolute_url(self):
        return reverse('accounts:profile',kwargs={'username':self.username})



