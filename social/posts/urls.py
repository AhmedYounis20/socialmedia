from django.urls import path
from django.urls.resolvers import URLPattern 
from . import views 
app_name='posts'
urlpatterns=[
    path('',views.FriendsPostsListView.as_view(),name='FriendsPost')
]