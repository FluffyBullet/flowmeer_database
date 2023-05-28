from django.db import models
from django.contrib.auth.models import User
from post.models import Post

class Comment(models.Model):
    """
    Table for comments relating to a users post
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    contnt = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content