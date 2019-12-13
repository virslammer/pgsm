from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

# Create your models here.
class ArticleCategory(models.Model):
	name = models.CharField(max_length=255, unique=True)
	slug = models.SlugField()
	cover_img = models.ImageField(upload_to=('static/blog/article-category-cover'))
	summary = models.TextField(default="default summary")
	def __str__(self):
		return self.name
	def save(self):
		self.slug = slugify(self.name)

	def get_absolute_url(self):
		return reverse("article-category", kwargs={"slug": self.slug})
	

class Article(models.Model):
	category = models.ForeignKey('ArticleCategory', on_delete=models.CASCADE)
	title = models.CharField(max_length=500, unique=True)
	slug = models.SlugField()
	created_date = models.DateTimeField(auto_now =True)
	updated_date = models.DateTimeField(auto_now_add=True) 
	cover = models.ImageField(upload_to="static/blog/article-cover")
	summary = models.TextField()
	content = models.TextField()
	hide = models.BooleanField(default=False)
	def get_absolute_url(self):
		return reverse("article-detail", kwargs={"slug": self.slug})
	

