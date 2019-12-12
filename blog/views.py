from django.shortcuts import render, get_object_or_404
from .models import ArticleCategory, Article
# Create your views here.
def home(request):
	context = {
	}
	return render(request,'blog/index.html',context)

def post_list(request,name):
	obj  = get_object_or_404(ArticleCategory, name=name)
	context = {
		'Category':obj
	}
	return render(request,'blog/list-posts.html',context)
def post_detail(request,id):

	article = get_object_or_404(Article, id=id)
	context = {
			'post':article
		}
	return render(request,'blog/single.html',context)