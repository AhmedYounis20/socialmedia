from django.urls import path
from django.urls.resolvers import URLPattern 
from . import views 
app_name='posts'
urlpatterns=[
    path('create/',views.CreatePostView.as_view(),name='createPost'),
    path('<slug:username>/post/<int:pk>/',views.postDetailView.as_view(),name='PostDetail'),
    path('',views.FriendsPostsListView.as_view(),name='FriendsPost'),
    path('<slug:username>/post/<int:pk>/delete',views.DeletePostView.as_view(),name='PostDelete'),
    path('<slug:username>/post/<int:pk>/update',views.UpdatePostView.as_view(),name='PostUpdate'),
    path('<slug:username>/post/<int:pk>/addcomment/',views.CreateCommentView.as_view(),name="addComment"),
    path('post/<int:post_id>/removecomment/<int:pk>',views.DeleteCommentView.as_view(),name="deleteComment"),
    path('post/<int:post_id>/editcomment/<int:pk>',views.UpdateCommentView.as_view(),name="UpdateComment"),

]