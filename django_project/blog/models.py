from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now) # auto_now will track every updation while auto_now_add will track time of creation
	author = models.ForeignKey(User, on_delete=models.CASCADE ) # what if user got deleted , should we put author as none or should we delete posts as well, here i a using second option

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail',kwargs={'pk' : self.pk })


