from django.db import models
from django.contrib.auth.models import User

class PostTags(models.Model):
	tag = models.CharField(max_length=50)

	def __str__(self):
		return self.tag	

class Post(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=250)
	content = models.TextField()
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)
	categories = models.ManyToManyField('PostTags', related_name="posts")

	def __str__(self):
		return self.title

class Comment(models.Model):
	author = models.OneToOneField(User, on_delete=models.CASCADE)
	post = models.ForeignKey('Post', on_delete=models.CASCADE)
	comment_body = models.TextField()

	def __str__(self):
		return self.post


