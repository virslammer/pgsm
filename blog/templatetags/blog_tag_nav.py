from django import template 
from blog.models import ArticleCategory
from django.contrib.auth.models import User
from django.core.files.storage import Storage, default_storage
register = template.Library()


@register.simple_tag
def blog_menu():
	menu = ArticleCategory.objects.all()
	return menu
@register.filter
def file_exists(filepath):
	# if default_storage.exists(filepath):
	# 	return filepath
	# else:
	# 	index = filepath.rfind('/')
	# 	new_filepath = filepath[:index] + '/image.png'
	# 	return new_filepath
	if filepath[-1] == '/':
		return filepath + 'image.png'
	else:
		return filepath
