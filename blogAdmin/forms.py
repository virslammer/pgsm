from django.forms import ModelForm 
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget

from .models import *
from blog.models import *

class AuthorForm(ModelForm):
    class Meta:
        model = AuthorProfile
        fields = '__all__'
        exclude = ['user']


class AuthorRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class ArticleCreateForm(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        exclude = ['author']

class ArticleUpdateForm(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        exclude = ['author']

class SettingForm(forms.Form):
    articles = forms.ModelChoiceField(queryset=Article.objects.filter(hide=False))