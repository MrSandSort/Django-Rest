from django.urls import path, include 
from . import views

urlpatterns=[path ("blogposts/", views.BlogPostListCreate.as_view(), name="blogpost-view-create"),
             path("blogposts/<int:pk>", views.BlogPostRetrieveUpdateDestroy.as_view(), name="update"),
             path("login/", views.login_view, name='login'),
             path("logout/",views.logout_view, name='logout'), 
             path('register/', views.register_view, name='register')]
