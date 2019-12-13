from django import template 
from blog.models import ArticleCategory
register = template.Library()


@register.simple_tag
def blog_menu():
	return ArticleCategory.objects.all()
