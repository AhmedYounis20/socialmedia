from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .forms import CreateAccountForm
# Create your views here.
from django.http import HttpResponse
from django.views.generic import CreateView,TemplateView
from .models import Account
from django.contrib.auth.models import User
from django.urls import reverse

class signupView(CreateView):
    form_class = CreateAccountForm
    success_url= reverse_lazy('login')
    template_name='signup.html'

class signinView(TemplateView):
    
    template_name='login.html'

def test(request):
    if Account.objects.filter(username=request.user).exists():
        return render(request,'test.html')
    else:
        return redirect(reverse('accounts:CreateAccount'))
def CreateAccount(request):
    user=User.objects.get(username='rami2')
    newAccount=Account(username=user.username,user=user)
    newAccount.save()

    return redirect(reverse('accounts:test'))