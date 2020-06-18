import json 

from django.forms import formset_factory
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group


from blog.models import Article

from .forms import AuthorRegisterForm, ArticleCreateForm, ArticleUpdateForm, SettingForm
from .models import AuthorProfile
from .decorators import unauthenticated_user, allowed_users, login_required
# from .filters import ArticleFilter

# Create your views here.
'''
----------------------------
		REGISTER / LOGIN / LOGOUT USER 
----------------------------

'''
@unauthenticated_user
def Register(request):
	form = AuthorRegisterForm()
	if request.method == 'POST':
		form = AuthorRegisterForm(request.POST)
		print(request.POST)
		if form.is_valid():
			user = form.save()
			user_name =  form.cleaned_data.get('username')
			group = Group.objects.get(name='author')
			user.groups.add(group)
			AuthorProfile.objects.create(user=user)
			messages.success(request, 'Tai khoan ' + user_name + ' da duoc tao thanh cong')
			return redirect(reverse('blogAdmin:login'))
	context = {'form':form}
	return render(request, 'blogAdmin/register.html', context)

@unauthenticated_user	
def LoginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect(reverse('blogAdmin:dashboard'))
		else:
			messages.info(request, 'Tai khoan hoac mat khau khong chinh xac')
	context = {}
	return render(request, 'blogAdmin/login.html', context)


def LogoutUser(request):
    logout(request)
    return redirect(reverse('blogAdmin:login'))

'''
----------------------------
		DASHBOARD
----------------------------

'''
@allowed_users(allowed_roles=['author','admin'])
def Dashboard(request):
	top_5_articles = Article.objects.all()
	last_5_articles = Article.objects.all().order_by('-created_date')[:5]
	context = {'top_5_articles':top_5_articles,
				'last_5_articles':last_5_articles,
				}
	return render(request, 'blogAdmin/dashboard.html', context)

'''
----------------------------
		CRUD ARTICLE
----------------------------

'''
@allowed_users(allowed_roles=['author','admin'])
def AllArticles(request):
	articles = Article.objects.all()
	aFilter = ArticleFilter(request.GET, queryset=articles)
	context = {
		'articles':articles,
		'article_filter' : aFilter}
	return render(request, 'blogAdmin/all-articles.html', context)

@allowed_users(allowed_roles=['author','admin'])
def CreateArticle(request):
	form = ArticleCreateForm()
	if request.method == 'POST':
		form = ArticleCreateForm(request.POST)
		author = request.user.author
		if form.is_valid():
			print(request.POST)
			instance = form.save(commit=False)
			instance.author = author
			instance.save()
			form.save_m2m()
			return redirect(reverse('blogAdmin:dashboard'))
	context = {'form':form}
	return render(request, 'blogAdmin/create-article.html', context)

@allowed_users(allowed_roles=['author','admin'])	
def UpdateArticle(request,pk):
	article = Article.objects.get(id=pk)
	form = ArticleUpdateForm(instance=article)
	if request.method == 'POST':
		form = ArticleUpdateForm(request.POST, instance=article)
		if form.is_valid():
			form.save()
			return redirect(reverse('blogAdmin:dashboard'))
	context = {'form':form}
	return render(request, 'blogAdmin/update-article.html', context)

@allowed_users(allowed_roles=['author','admin'])
def DeleteArticle(request,pk):
	article = Article.objects.get(id=pk)
	if request.method == 'POST':
		article.delete()
		return redirect(reverse('blogAdmin:dashboard'))
	context = {'article':article}
	return render(request, 'blogAdmin/delete-article.html', context)

'''
----------------------------
		EXTRA
----------------------------

'''

@allowed_users(allowed_roles=['admin'])
def BlogSetting(request):
	pass
def About(request, user):
	pass