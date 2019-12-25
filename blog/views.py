from django.shortcuts import render, get_object_or_404
from .models import ArticleCategory, Article,Profile
from django.contrib.auth.models import User
from django.core.paginator import Paginator
# Create your views here.
def home(request):

	# Home page items 
	main_articles = Article.objects.filter(hide=False).order_by('-created_date')[:5]
	all_articles =Article.objects.filter(hide=False).order_by('-created_date')
	paginator = Paginator(all_articles,9)
	page = request.GET.get('page')
	article_list = paginator.get_page(page)
	context = {
		'main_articles':main_articles,
		'article_list':article_list
	}
	return render(request,'blog/index.html',context)



def article_list(request,slug):
	obj  = get_object_or_404(ArticleCategory, slug=slug)
	
	a_list = obj.article_set.filter(hide=False)
	paginator = Paginator(a_list,3)
	page = request.GET.get('page')
	article_list = paginator.get_page(page)
	context = {
		'category':obj,
		'article_list':article_list
	}
	return render(request,'blog/list-posts.html',context)
def article_detail(request,slug):

	article = get_object_or_404(Article, slug=slug, hide=False)
	related_articles = Article.objects.filter(category=article.category, hide=False)
	context = {
			'article':article,
			'related_articles': related_articles
		}
	return render(request,'blog/single.html',context)

def about(request, user):
	user = get_object_or_404(User, username=user)
	user_profile = Profile.objects.get(user=user)
	context = {
		'user_profile':user_profile
	}
	return render(request, 'blog/about.html',context)