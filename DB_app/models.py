from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Author(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    author_rating = models.IntegerField(default=0)

    def update_rating(self):
        post_rating_sum = Post.objects.filter(author=self)


class Category(models.Model):
    category_name = models.CharField(max_length=255, unique=True)


class Post(models.Model):
    post_type_choices = (('ne', 'Новость'), ('ar', 'Статья'))
    post_type = models.CharField(max_length=2, choices=post_type_choices)
    post_name = models.CharField(max_length=255)
    post_text = models.CharField()
    post_time = models.DateTimeField(auto_now_add=True)
    post_rating = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, through='PostCategory')

    def post_like(self):
        self.post_rating += 1
        self.save()

    def post_dislike(self):
        self.post_rating -= 1
        self.save()


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    comment_text = models.CharField()
    comment_time = models.DateTimeField(auto_now_add=True)
    comment_rating = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def comment_like(self):
        self.comment_rating += 1
        self.save()

    def comment_dislike(self):
        self.comment_rating -= 1
        self.save()
