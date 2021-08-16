from accounts.models import Account
from django.contrib import admin
from .models import *
admin.site.register(Account)
admin.site.register(Post)
admin.site.register(Group)



