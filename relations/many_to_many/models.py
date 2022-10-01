from django.db import models


# Create your models here.
class Publication(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Article(models.Model):
    publications = models.ManyToManyField(Publication)
    headline = models.CharField(max_length=100)

    def __str__(self):
        return self.headline