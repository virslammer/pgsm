from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

class AuthorProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
	nick_name = models.CharField(max_length=50,default='none', blank=True)
	bio = RichTextField()
	fb_link = models.CharField(max_length=250, blank=True, verbose_name="Facebook")
	address = models.TextField(blank=True )
	birth_date = models.DateField(null=True, blank=True)
	profile_pic = models.ImageField( upload_to="user/profile-pic", blank=True, verbose_name="Avatar")
	cover_pic = models.ImageField( upload_to="user/cover-pic", blank=True, verbose_name="Cover")
	def __str__(self):
		return self.user.username # Create your models here.
	
	@property
	def profile_pic_url(self):
		try:
			return self.profile_pic.url
		except:
			return ''
	@property
	def cover_pic_url(self):
		try:
			return self.cover_pic.url
		except:
			return ''

	class Meta:
		verbose_name = "AuthorProfile"
		verbose_name_plural = "AuthorProfile"