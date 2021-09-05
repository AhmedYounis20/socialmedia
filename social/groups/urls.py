from django.urls import path
from . import views
app_name='groups'
urlpatterns=[
path('createGroup/',views.CreateGroupView.as_view(),name='createGroup'),
path('<slug:username>/groups/',views.ListGroupView.as_view(),name='ListGroup'),
path('<int:pk>/',views.groupDetailView.as_view(),name='GroupDetail'),
path('<int:pk>/delete/',views.DeleteGroupView.as_view(),name='DeleteGroup'),
]