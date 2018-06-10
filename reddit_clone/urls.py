from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('', views.sub_reddit_list, name='sub_reddit_list'),
    path('sub/', views.sub_reddit_list, name='sub_reddit_list'),
    path('sub/<int:pk>', views.sub_reddit_detail, name='sub_reddit_detail'),
    path('sub/new', views.sub_create, name='sub_create'),
    path('posts/', views.post_list, name='post_list'),
    path('comments/',views.comment_list, name='comment_list'),
    path('comments/new', views.comment_create, name='comment_create'),
    path('posts/new', views.post_create, name='post_create'),
]