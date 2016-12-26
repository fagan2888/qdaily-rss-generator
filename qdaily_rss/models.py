from django.db import models
from django.utils.timezone import now

class Article(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField()
    url = models.URLField()
    description = models.TextField()
    crawled = models.DateTimeField(default=now())
