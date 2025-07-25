from django.db import models

# Create your models here.
class Post(models.Model):
    name=models.CharField(max_length=100)
    roll=models.IntegerField()

    def __str__(self):
        return self.name