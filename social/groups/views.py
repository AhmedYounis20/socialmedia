from django.forms.models import ModelMultipleChoiceField
from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView,ListView,DeleteView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from accounts.models import Account
from .models import *
from posts.models import Post
from django.urls import reverse_lazy

class CreateGroupView(CreateView,LoginRequiredMixin):
    model=Group
    template_name='groups/group_form.html'

    fields=['name','description','slug']

    def form_valid(self, form):
        object=form.save(commit=False)
        object.owner=Account.objects.get(user=self.request.user)
        
        object.save()
        member=Membership()
        member.account=Account.objects.get(user=self.request.user)
        member.group=object
        member.accept()
        member.save()
        return super().form_valid(form)


class ListGroupView(ListView,LoginRequiredMixin):
    model=Group
    def get_queryset(self) :
        username=self.request.user
        userAccount=Account.objects.get(username=username)
        groups=Group.objects.filter(members__in=[userAccount])
        return groups
    def get_context_data(self, **kwargs):
        
        data=super().get_context_data(**kwargs)
        data['username']=self.kwargs['username']
        return data
    context_object_name='userGroups'
        
class groupDetailView(DetailView,LoginRequiredMixin):
    model=Group


class DeleteGroupView(DeleteView,LoginRequiredMixin):
    model=Group
    def get_success_url(self) -> str:
        return reverse('groups:ListGroup',kwargs={'username':self.request.user.username})

    template_name='groups/group_confirm_delete.html'
    def get_context_data(self, **kwarg):
        data=super().get_context_data(**kwarg)
        print(self.success_url)
        return super().get_context_data(**kwarg)
    
