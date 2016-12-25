from django.db import models
import datetime

class Article(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField()
    url = models.URLField()
    description = models.TextField()
    crawled = models.DateField(default=datetime.date.today)
