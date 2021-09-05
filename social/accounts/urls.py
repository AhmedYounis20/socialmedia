from django.contrib.auth import logout
from django.urls import path
from django.views.generic.base import TemplateView
from . import views

from django.contrib.auth.views import LoginView,LogoutView



app_name="accounts"
urlpatterns=[
    path('signup',views.signupView.as_view(),name='signup'),
    path('login/',LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('createAccount/',views.CreateAccount,name='CreateAccount'),    
    path('test/',views.test,name='test'),

]