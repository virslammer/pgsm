from django.contrib import admin
from django.urls import path
from blog.views import *

app_name = 'blog'
urlpatterns = [
    path('', home, name='home-page'),
    path('post-list-<str:name>/', article_list, name='article-list'),
    path('post-detail/<int:id>/', article_detail, name='article-detail'),
]
