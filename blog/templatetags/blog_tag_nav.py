from django import template 
from blog.models import ArticleCategory, Profile
from django.contrib.auth.models import User
register = template.Library()


@register.simple_tag
def blog_menu():
	menu = ArticleCategory.objects.all()
	return menu
@register.simple_tag
def blog_profile():
	user = User.objects.get(username='minhanh')
	profile = Profile.objects.get(user=user)
	return profile