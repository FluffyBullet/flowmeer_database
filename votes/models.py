from django.db import models
from django.contrib.auth.models import User
from post.models import Post

# Create your models here.


class Vote(models.Model):
    """
    Grants the ability of users to +1 vote for the post/image
    """

    owner = models.ForeignKey(User, on_delete=models.CACSADE)
    post = models.ForeignKey(Post, related_name='votes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'post']

        def __str__(self):
            return f'{self.owner} {self.post}'