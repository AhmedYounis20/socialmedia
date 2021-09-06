from django.urls import path
from . import views
app_name='groups'
urlpatterns=[
path('createGroup/',views.CreateGroupView.as_view(),name='createGroup'),
path('<slug:username>/groups/',views.UserListGroupView.as_view(),name='UserListGroup'),
path('',views.ListGroupView.as_view(),name='ListGroup'),
path('<int:pk>/',views.groupDetailView.as_view(),name='GroupDetail'),
path('<int:pk>/update/',views.UpdateGroupView.as_view(),name='UpdateGroup'),
path('<int:pk>/delete/',views.DeleteGroupView.as_view(),name='DeleteGroup'),

]