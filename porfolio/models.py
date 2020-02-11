from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Porfolio(models.Model):
    title = models.CharField(max_length=150, unique=True)
    cover = models.ImageField(upload_to='porfolio/cover')
    content = models.RichTextField()
    def __str__(self):
        return self.title