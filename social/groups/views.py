from django.forms.models import ModelMultipleChoiceField
from django.shortcuts import redirect, render

# Create your views here.
from django.views.generic import DetailView,ListView,DeleteView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from accounts.models import Account
from .models import *
from posts.models import Post
from groups.models import Group
from django.urls import reverse_lazy
from django.shortcuts import get_list_or_404

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


class UserListGroupView(ListView,LoginRequiredMixin):
    model=Group
    template_name='groups/user_group_list.html'
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
class ListGroupView(ListView,LoginRequiredMixin):
    model=Group
    template_name='groups/group_list.html'
    def get_context_data(self, **kwargs):
        ctx=super().get_context_data(**kwargs)
        ctx['Account']=Account.objects.get(user=self.request.user)
        return ctx

class groupDetailView(DetailView,LoginRequiredMixin):
    model=Group
    template_name='groups/group_detail.html'
    def get_context_data(self, **kwargs):
        data=super().get_context_data(**kwargs)
        data['account']=Account.objects.get(user=self.request.user)
        return data   

class UpdateGroupView(UpdateView,LoginRequiredMixin):
    model=Group
    fields=['name','description','slug']
    
class DeleteGroupView(DeleteView,LoginRequiredMixin):
    model=Group
    def get_success_url(self) -> str:
        return reverse('groups:ListGroup',kwargs={'username':self.request.user.username})

    template_name='groups/group_confirm_delete.html'
    def get_context_data(self, **kwarg):
        data=super().get_context_data(**kwarg)
        print(self.success_url)
        return super().get_context_data(**kwarg)
    
class addPostView(CreateView,LoginRequiredMixin):
    model=Post
    fields=['text']
    template_name='posts/post_form.html'
    def form_valid(self,form):
        object=form.save(commit=False)
        object.owner=Account.objects.get(user=self.request.user)
        object.group=Group.objects.get(slug=self.kwargs['groupslug'])
        object.publish()
        object.save()
        return super().form_valid(form)
def joinGroup(request):
    if request.method == 'POST':
        group=Group.objects.get(id=request.POST['pk'])
        g=group.id
        account=Account.objects.get(id=request.POST['account_id'])
        group.members.add(account)
        group.save()
        return redirect('/groups/{}'.format(request.POST['pk']))
    else:
        return redirect(reverse('groups:ListGroup'))
def leaveGroup(request):
    if request.method == 'POST':
        group=Group.objects.get(id=request.POST['pk'])
        g=group.id
        account=Account.objects.get(id=request.POST['account_id'])
        group.members.remove(account)
        group.save()
    return redirect(reverse('groups:ListGroup'))    