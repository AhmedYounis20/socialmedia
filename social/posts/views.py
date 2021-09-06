from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView,UpdateView,DeleteView,DetailView
from django.contrib.auth.mixins import  LoginRequiredMixin
from accounts.models import Account
from .models import Post 

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






# Create your views here.

