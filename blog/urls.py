from django.contrib import admin
from django.urls import path
from blog.views import *


urlpatterns = [
    path('', Home, name='home-page'),
    path('article-category/<str:slug>', ArticleList, name='article-category'),
    path('<str:slug>', ArticleDetail, name='article-detail'),
    path('article-search/', ArticleSearch, name='article-search'),
    path('about/', About, name='about'),
]
