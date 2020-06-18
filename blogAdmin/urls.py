from django.contrib import admin
from django.urls import path
from blogAdmin.views import *

urlpatterns = [
    path('', Dashboard, name='dashboard'),
    path('login', LoginPage, name='login'),
    path('logout', LogoutUser, name='logout'),
    path('register', Register, name='register'),
    path('all-articles', AllArticles, name='all-articles'),
    path('create', CreateArticle, name='create-article'),
    path('update/<str:pk>', UpdateArticle, name='update-article'),
    path('delete/<str:pk>', DeleteArticle, name='delete-article'),

    path('setting', BlogSetting , name='blog-setting'),
    path('about',About , name='about')
]
