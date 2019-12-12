from django import template 
from blog.models import PostCategory
register = template.Library()


@register.simple_tag
def blog_menu():
	return PostCategory.objects.all()
