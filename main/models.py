from django.db import models

# Create your models here.


class Post(models.Model):
    code = models.CharField(max_length=100)
    content = models.TextField()
    image = models.TextField()

    def __str__(self):
        return self.code
