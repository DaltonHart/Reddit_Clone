from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

#customuser model
class CustomUser(AbstractUser):
    # First/last name is not a global-friendly pattern
    name = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.username

#class for created pages with posts
class Sub_Reddit (models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sub_reddits')
    description = models.TextField()

    def __str__(self):
        return self.name

class Post (models.Model):
    body = models.TextField()
    title = models.CharField(max_length=100)
    sub_reddit = models.ForeignKey(Sub_Reddit, on_delete=models.CASCADE, related_name='posts')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='posts', blank=True)

    def __str__(self):
        return self.title

# class Comment (models.Model):
#     user = 
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
#     body = models.TextField()
#     sub_comment = models.ManyToManyField('self', related_name='sub_comment', blank=True)

#     def __str__(self):
#         return self.post