from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    pass


class Category(models.Model):
    category_name = models.CharField(max_length=255, unique=True)
    pass


class Post(models.Model):
    post_name = models.CharField(max_length=255)
    post_text = models.CharField()
    post_rating = models.FloatField(default=0.0)
    post_time = models.DateTimeField(auto_now_add=True)
    pass


class PostCategory(models.Model):
    pass


class Comment(models.Model):
    pass
