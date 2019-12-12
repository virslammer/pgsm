from django.db import models

# Create your models here.
class PostCategory(models.Model):
	name = models.CharField(max_length=255, unique=True)
	summary = models.TextField(default="default summary")
	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return f"/blog/post-list-%s"%(self.name)

class Post(models.Model):
	category = models.ForeignKey('PostCategory', on_delete=models.CASCADE)
	subject = models.CharField(max_length=500, unique=True)
	create_date= models.DateTimeField(auto_now_add=True)
	summary = models.TextField()
	cover = models.ImageField(upload_to="static/blog/post_cover")
	content = models.TextField()

