from django.urls import path
from django.urls.resolvers import URLPattern 
from . import views 
app_name='posts'
urlpatterns=[
    path('create/',views.CreatePostView.as_view(),name='createPost'),
    path('<slug:username>/post/<int:pk>/',views.postDetailView.as_view(),name='PostDetail'),
    path('',views.FriendsPostsListView.as_view(),name='FriendsPost'),

]