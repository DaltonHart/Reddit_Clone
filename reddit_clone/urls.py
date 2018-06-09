from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('', views.sub_reddit_list, name='sub_reddit_list'),
    path('sub/<int:pk>', views.sub_reddit_detail, name='sub_reddit_detail'),
]