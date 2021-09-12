from django import template
from django.contrib.auth import logout
from django.urls import path
from django.views.generic.base import TemplateView,RedirectView
from . import views

from django.contrib.auth.views import LoginView,LogoutView



app_name="accounts"
urlpatterns=[
    path('<slug:username>/profile/',views.Profile.as_view(),name='profile'),
    path('signup/',views.signupView.as_view(),name='signup'),
    path('login/',LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('createAccount/',views.CreateAccount,name='CreateAccount'),
    path('<slug:username>/profile/edit/<int:pk>',views.EditAccountView.as_view(),name='editProfile'),
    path('done/',views.ProfileRedirect,name='test'),

]