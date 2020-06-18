from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.core.paginator import Paginator


from .models import ArticleCategory, Article, BlogInfo
from blogAdmin.models import AuthorProfile
import json 
# Create your views here.


'''
----------------------------
		HOME PAGE
----------------------------

'''

def Home(request):
	BLOG_INFO = BlogInfo.objects.get(name='PGSM')
	def get_article_by_remark(remark):
		try:
			return Article.objects.filter(remark=remark,hide=False).order_by('-updated_date')[0]
		except:
			return []
	main_articles = {
		'middle':get_article_by_remark('home-middle'),
		'top_left':get_article_by_remark('home-left-top'),
		'bottom_left':get_article_by_remark('home-left-bottom'),
		'top_right':get_article_by_remark('home-right-top'),
		'bottom_right':get_article_by_remark('home-right-bottom')
	}
	
	all_articles =Article.objects.filter(hide=False).order_by('-updated_date')
	paginator = Paginator(all_articles,BLOG_INFO.number_of_article)
	if BLOG_INFO.number_of_article < 1:
		paginator = Paginator(all_articles,1)
	page = request.GET.get('page')
	article_list = paginator.get_page(page)
	context = {
		'main_articles':main_articles,
		'article_list':article_list
	}
	return render(request,'blog/index.html',context)

'''
----------------------------
		DISPLAY
----------------------------

'''

def ArticleList(request,slug):
	BLOG_INFO = BlogInfo.objects.get(name='PGSM')
	obj  = get_object_or_404(ArticleCategory, slug=slug)
	a_list = obj.article_set.filter(hide=False).order_by('-updated_date')
	paginator = Paginator(a_list,BLOG_INFO.number_of_page_category)
	if BLOG_INFO.number_of_page_category < 1:
		paginator = Paginator(a_list,1)
	page = request.GET.get('page')
	article_list = paginator.get_page(page)
	context = {
		'category':obj,
		'article_list':article_list
	}
	return render(request,'blog/list-posts.html',context)

def ArticleDetail(request,slug):

	article = get_object_or_404(Article, slug=slug, hide=False)
	related_articles = Article.objects.filter(category=article.category, hide=False)
	context = {
			'article':article,
			'related_articles': related_articles
		}
	return render(request,'blog/single.html',context)

def ArticleSearch(request):
	result = Article.objects.filter(title__icontains=request.GET['key'])
	context = {
		'article_list':result
	}
	return render(request, 'blog/search-list.html',context)
'''
----------------------------
		About (Temp)
----------------------------

'''
def About(request):
	user = get_object_or_404(User, username='minhanh')
	user_profile = get_object_or_404(AuthorProfile, user=user)
	context = {
		'profile':user_profile
	}
	return render(request,'blog/about.html',context)