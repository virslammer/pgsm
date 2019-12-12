from django.shortcuts import render, get_object_or_404
from .models import PostCategory, Post
# Create your views here.
def home(request):
	context = {
	}
	return render(request,'blog/index.html',context)

def post_list(request,name):
	obj  = get_object_or_404(PostCategory, name=name)
	context = {
		'Category':obj
	}
	return render(request,'blog/list-posts.html',context)
def post_detail(request,id):

	post = get_object_or_404(Post, id=id)
	context = {
			'post':post
		}
	return render(request,'blog/single.html',context)