from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Articles(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=False, null=False)
    content = models.CharField(max_length=3000, blank=False, null=False)
    last_update = models.DateTimeField(default=timezone.now)
    Articles_CHOICES = (('post','留言'),('share','分享'),('mood','心情'),('question','請益'))
    type = models.CharField(max_length=20, choices=Articles_CHOICES)
    class Meta:
        db_table = 'Articles'
        ordering = ('-last_update',)

class Comment(models.Model):
    article = models.ForeignKey(Articles, on_delete=models.CASCADE, related_name='comments')
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_content = models.CharField(max_length=300, blank=False, null=False)
    comment_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.article)
    class Meta:
        db_table = 'Comment'
        ordering = ('-comment_date',)