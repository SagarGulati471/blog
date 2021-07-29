from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)  
    author=models.ForeignKey(User,on_delete=models.CASCADE)  #Foreign key because one author can have multiple posts

    def __str__(self):         #This is a dunder function (dunder func are double underscores functions or special built in functions)
        return self.title   

    
    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})