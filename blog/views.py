from django.shortcuts import render, get_object_or_404
from .models import ArticleCategory, Article
# Create your views here.
def home(request):
	context = {
	}
	return render(request,'blog/index.html',context)

def article_list(request,slug):
	obj  = get_object_or_404(ArticleCategory, slug=slug)
	article_list = obj.article_set.all()
	context = {
		'category':obj,
		'article_list':article_list
	}
	return render(request,'blog/list-posts.html',context)
def article_detail(request,slug):

	article = get_object_or_404(Article, slug=slug)
	context = {
			'article':article
		}
	return render(request,'blog/single.html',context)