from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User
from unidecode import unidecode

# Create your models here.
class ArticleCategory(models.Model):
	name = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(default='',editable=False)
	cover_img = models.ImageField(upload_to=('blog/article-category-cover'))
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
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE) 
	cover = models.ImageField(upload_to="blog/article-cover")
	summary = models.TextField()
	content = models.TextField()
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
	
# Extend  User model
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.TextField(max_length=500, blank=True)
	address = models.TextField(blank=True)
	birth_date = models.DateField(null=True, blank=True)
	def __str__(self):
		return self.user







