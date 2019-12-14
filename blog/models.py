from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

# Create your models here.
class ArticleCategory(models.Model):
	name = models.CharField(max_length=255, unique=True)
	slug = models.SlugField(null=False, unique=True)
	cover_img = models.ImageField(upload_to=('static/blog/article-category-cover'))
	summary = models.TextField(default="default summary")
	class Meta:
		verbose_name = "Article Category"
		verbose_name_plural = "Article Categories"
	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("blog:article-category", kwargs={"slug": self.slug})
	def save(self, *args, **kwargs): 
		if not self.slug:
			self.slug = slugify(self.name)
		return super().save(*args, **kwargs)
	

class Article(models.Model):
	category = models.ForeignKey('ArticleCategory', on_delete=models.CASCADE)
	title = models.CharField(max_length=500, unique=True)
	slug = models.SlugField(null=False, unique=True)
	created_date = models.DateTimeField(auto_now_add =True)
	updated_date = models.DateTimeField(auto_now=True) 
	cover = models.ImageField(upload_to="static/blog/article-cover")
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
			self.slug = slugify(self.title)
		return super().save(*args, **kwargs)
	

