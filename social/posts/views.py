from django.forms import forms
from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView,UpdateView,DeleteView,DetailView
from django.contrib.auth.mixins import  LoginRequiredMixin
from accounts.models import Account
from .models import Post , Comment
from django.urls import reverse
class CreatePostView(CreateView,LoginRequiredMixin):
    model=Post
    fields=['text']
    template_name='posts/post_form.html'
    def form_valid(self,form):
        object=form.save(commit=False)
        object.owner=Account.objects.get(user=self.request.user)
        object.publish()
        object.save()
        return super().form_valid(form)
class postDetailView(DetailView,LoginRequiredMixin):
    model=Post
    template_name='posts/post.html'
class FriendsPostsListView(ListView,LoginRequiredMixin):

    
    model=Post
    def get_context_data(self, **kwargs):
        ctx=super().get_context_data(**kwargs)
        all_posts=ctx['post_list']
        friends_post_list=[]
        user_account=Account.objects.get(username=self.request.user)
        for post in all_posts:
            if user_account.friends.values().filter(username=post.owner.username).exists():
                if post.group ==None or user_account.objects.filter(group__in=[post.group]) :
                    if post not in friends_post_list:
                        friends_post_list.append(post) 
            elif post.owner.username==user_account.username:
                    if post not in friends_post_list:
                        friends_post_list.append(post)                
        ctx['post_list']= friends_post_list
        return ctx
    template_name='posts/post_list.html'


class UpdatePostView(UpdateView,LoginRequiredMixin):
    model=Post
    fields=['text']
    def get_queryset(self):
        return super().get_queryset().filter(owner=Account.objects.get(user=self.request.user))
    template_name='posts/post_form.html'


class DeletePostView(DeleteView,LoginRequiredMixin):
    model=Post
    def get_queryset(self):
        return super().get_queryset().filter(owner=Account.objects.get(user=self.request.user))
    template_name='posts/post_confirm_delete.html'

    


class CreateCommentView(CreateView,LoginRequiredMixin):
    model=Comment
    fields=['text']
    def get_success_url(self):
        return reverse('posts:PostDetail' , kwargs={'username':self.get_queryset()[0].owner.username,'pk':self.kwargs['pk']})
    def form_valid(self, form):
        comment=form.save(commit=False)
        comment.owner=Account.objects.get(user=self.request.user)
        comment.post=Post.objects.get(id=self.request.POST['post_id'])
        comment.publish
        comment.save()
        return super().form_valid(form)
    template_name='posts/post.html'
class DeleteCommentView(DeleteView,LoginRequiredMixin):
    model=Comment
    template_name='posts/post_confirm_delete.html'
    def get_context_data(self, **kwargs ):
        data=super().get_context_data(**kwargs)
        data['post']=Post.objects.get(id=self.kwargs['post_id'])
        return data
    def get_queryset(self):
        return super().get_queryset().filter(owner=Account.objects.get(user=self.request.user))
    def get_success_url(self):
        return reverse('posts:PostDetail' , kwargs={'username':self.get_queryset()[0].owner.username,'pk':self.kwargs['post_id']})
class UpdateCommentView(UpdateView,LoginRequiredMixin):
    model=Comment
    fields=['text']
    template_name='posts/comment_form.html'
    def form_valid(self, form): 
        object=form.save(commit=False)
        object.publish()
        return super().form_valid(form)
    def get_context_data(self, **kwargs ):
        data=super().get_context_data(**kwargs)
        data['post']=Post.objects.get(id=self.kwargs['post_id'])
        return data
    def get_success_url(self):
        return reverse('posts:PostDetail' , kwargs={'username':self.get_queryset()[0].owner.username,'pk':self.kwargs['post_id']})
# Create your views here.

