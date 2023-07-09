from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    favorite_numbers = models.IntegerField(default=0)
    disgust_numbers = models.IntegerField(default=0)
    is_shown = models.BooleanField(default=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post',on_delete=models.CASCADE,related_name='comments')
    reader = models.CharField(max_length=200)
    comment_text = models.TextField()
    agreed_numbers = models.IntegerField(default=0)
    disgust_numbers = models.IntegerField(default=0)
    approved_comment = models.BooleanField(default=False)
    created_date = models.DateTimeField(
        default=timezone.now)

    def approve(self):
        self.approved_comment=True
        self.save()

    def __str__(self):

        return self.comment_text

