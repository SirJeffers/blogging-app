import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

#author model, each author has a name and bio
class Author(models.Model):
    auth_name = models.CharField(max_length=30)
    auth_bio = models.CharField(max_length=128)
    def __str__(self):
        return self.auth_name

#Post model, each post has a title, link to the author
#as well as a the posts information and date of creation
class Post(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_author= models.ForeignKey(Author, on_delete=models.CASCADE)
    blog_post = models.CharField(max_length=1000)
    blog_date = models.DateTimeField('date blog was published')
    def __str__(self):
        return self.blog_title

