from django.db import models

class Article(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField()
    url = models.URLField()
    description = models.TextField()
    crawled = models.DateTimeField()
