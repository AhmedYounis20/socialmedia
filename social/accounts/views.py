from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import CreateAccountForm
# Create your views here.
from django.views.generic import CreateView,TemplateView




class signupView(CreateView):
    form_class = CreateAccountForm
    success_url= reverse_lazy('login')
    template_name='signup.html'

class signinView(TemplateView):
    
    template_name='login.html'