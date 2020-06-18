from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User
from unidecode import unidecode
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.signals import pre_save

class BlogInfo(models.Model):
	name = models.CharField(max_length=50, default='PGSM',unique=True)
	logo = models.ImageField(upload_to='blog/favicon')
	number_of_article = models.IntegerField(default=9,  help_text="number of article will be showed in home page",  null=True, blank=True)
	number_of_article_category = models.IntegerField(default=9,  help_text="number of article will be showed in category page",  null=True, blank=True)
	def __str__(self):
		return self.name
	class Meta:
		verbose_name = "Blog information"
		verbose_name_plural = "Blog information"

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
	category = models.ForeignKey(ArticleCategory, on_delete=models.SET_NULL, null=True, blank=True)
	author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, default=None) 
	title = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(default='',unique=True,blank=True, null=True)
	created_date = models.DateTimeField(auto_now_add =True)
	updated_date = models.DateTimeField(auto_now=True)
	cover = models.ImageField(upload_to="blog/article-cover",default='blogAdmin/default-cover-article/default-cover.jpg',blank=True)
	summary = models.TextField()
	content = RichTextUploadingField()
	tag = models.CharField( max_length=250,blank=True)
	hide = models.BooleanField(default=False)
	remark = models.CharField( max_length=250,blank=True,null=True)


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
	
	@property
	def	cover_url(self):
		try:
			return self.cover.url
		except:
			return ''
	








