from django.contrib import admin
from django.urls import path
from blog.views import *

app_name = 'blog'
urlpatterns = [
    path('', home, name='home-page'),
    path('article-category/<str:slug>', article_list, name='article-category'),
    path('<str:slug>', article_detail, name='article-detail'),
    path('about/<str:user>',about, name='about')
]
