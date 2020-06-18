from django.contrib import admin
from .models import AuthorProfile
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    pass 
admin.site.register(AuthorProfile, AuthorAdmin)