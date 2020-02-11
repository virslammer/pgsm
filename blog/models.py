from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User
from unidecode import unidecode
from ckeditor.fields import RichTextField



class BlogInfo(models.Model):
	name = models.CharField(max_length=50, default='PGSM',unique=True)
	logo = models.ImageField(upload_to='blog/favicon')

	def __str__(self):
		return self.name
	class Meta:
		verbose_name = "Blog information"
		verbose_name_plural = "Blog information"
# Extend  User model
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	nick_name = models.CharField(max_length=50,default='')
	bio = RichTextField()
	fb_link = models.CharField(max_length=250, blank=True, verbose_name="Facebook")
	address = models.TextField(blank=True )
	birth_date = models.DateField(null=True, blank=True)
	profile_pic = models.ImageField( upload_to="user/profile-pic", blank=True, verbose_name="Avatar")
	cover_pic = models.ImageField( upload_to="user/cover-pic", blank=True, verbose_name="Cover")
	def __str__(self):
		return self.user.username # Create your models here.

	def get_absolute_url(self):
		return reverse("blog:about", kwargs={"user": self.user.username})
	class Meta:
		verbose_name = "Profile"
		verbose_name_plural = "Profile"
	


class ArticleCategory(models.Model):
	name = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(default='',editable=False)
	cover_img = models.ImageField(upload_to='blog/article-category-cover')
	summary = models.TextField(default="default summary")

	class Meta:
		verbose_name = "Article Category"
		verbose_name_plural = "Article Categories"
	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse("blog:article-category", kwargs={"slug": self.slug})
	def save(self, *args, **kwargs): 
		self.slug = slugify(unidecode(self.name)) # Xoa dau tieng viet
		return super().save(*args, **kwargs)


class Article(models.Model):
	category = models.ForeignKey('ArticleCategory', on_delete=models.CASCADE)
	title = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(default='',editable=False)
	created_date = models.DateTimeField(auto_now_add =True)
	updated_date = models.DateTimeField(auto_now=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE, default='') 
	cover = models.ImageField(upload_to="blog/article-cover")
	summary = models.TextField()
	content = RichTextField()
	tag = models.CharField( max_length=250,blank=True)
	hide = models.BooleanField(default=False)
	class Meta:
		verbose_name = "Article"
		verbose_name_plural = "Articles"
	def __str__(self):
		return self.title
	def get_absolute_url(self):
		return reverse("blog:article-detail", kwargs={"slug": self.slug})
	def save(self, *args, **kwargs): 
		if not self.slug:
			self.slug = slugify(unidecode(self.title))
		return super(Article, self).save(*args, **kwargs)
	








