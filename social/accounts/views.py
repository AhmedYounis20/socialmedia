from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from .forms import CreateAccountForm,UpdateProfile
# Create your views here.
from django.http import HttpResponse
from django.views.generic import CreateView,TemplateView,RedirectView
from .models import Account
from django.contrib.auth.models import User
from groups.models import Group
from posts.models import Post
from django.urls import reverse
from django.contrib.auth.decorators import login_required
class signupView(CreateView):
    form_class = CreateAccountForm
    success_url= reverse_lazy('login')
    template_name='signup.html'

class signinView(TemplateView):
    
    template_name='login.html'
@login_required
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
class EditAccountView(UpdateView,LoginRequiredMixin):
    model=Account
    form_class=UpdateProfile
    def get_context_data(self, **kwargs):
        data=super().get_context_data(**kwargs)
        data['Account']=Account.objects.get(user=self.request.user)
        return data
    template_name='signup.html'
class Profile(TemplateView,LoginRequiredMixin):
    template_name='profile.html'
    def get_context_data(self, **kwargs):
        data=super().get_context_data(**kwargs)
        data["Account"]=Account.objects.get(user=self.request.user)
        data['Posts']=Post.objects.filter(owner=data['Account']).order_by('-published_at')
        data['Groups']=Group.objects.filter(members__in=[data['Account']])
        return data
@login_required
def ProfileRedirect(request):
    
    return redirect(reverse('accounts:profile',kwargs={'username':request.user.username}))