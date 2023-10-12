from django.db import models

# Create your models here.


class Post(models.Model):
    code = models.CharField(max_length=100)
    content = models.TextField()
    image = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.code
