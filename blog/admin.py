from django.contrib import admin
from .models import ArticleCategory,Article,  Profile, BlogInfo
from django.contrib.auth.models import User
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug','summary' ]
    
class ArticleAdmin(SummernoteModelAdmin):
    list_display = ['title','category','created_date','updated_date','slug', 'hide']
    list_editable = ['hide']
    list_filter = ['category']
    summernote_fields = ('content')
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'author':
            kwargs['queryset'] = User.objects.filter(username=request.user.username)
        return super(ArticleAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            return self.readonly_fields + ('author',)
        return self.readonly_fields

    def add_view(self, request, form_url="", extra_context=None):
        data = request.GET.copy()
        data['author'] = request.user
        request.GET = data
        return super(ArticleAdmin, self).add_view(request, form_url="", extra_context=extra_context)

admin.site.register(BlogInfo)
admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Profile)