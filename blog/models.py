from django.db import models
from django.db.models.deletion import CASCADE
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.
from django.shortcuts import render,redirect,reverse,resolve_url,get_object_or_404

class Post(models.Model):

    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(User,on_delete=models.SET_NULL,related_name="posts",null = True)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(default="", null=False, editable=False,)
    fake = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-list-page")
    


class Comment(models.Model):
    user_name = models.CharField(max_length=150)
    text = models.TextField()
    post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name="comments")
