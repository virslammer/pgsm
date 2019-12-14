from django.contrib import admin
from .models import ArticleCategory,Article

# Register your models here.

class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ['name','summary']
    
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','category','created_date','updated_date','slug', 'hide']
    list_editable = ['hide']
    list_filter = ['category']

admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Article, ArticleAdmin)