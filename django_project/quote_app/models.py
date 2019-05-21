from django.db import models

# Create your models here.
class Quote(models.Model):
    title = models.TextField()
    author = models.CharField(max_length=100)
    tags = models.ManyToManyField('Tag')

class Tag(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
