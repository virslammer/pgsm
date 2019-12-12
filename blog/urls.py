from django.contrib import admin
from django.urls import path
from blog.views import *

urlpatterns = [
    path('', home, name='home-page'),
    path('post-list-<str:name>/', post_list, name='post-list'),
    path('post-detail/<int:id>/', post_detail, name='post-detail'),
]
