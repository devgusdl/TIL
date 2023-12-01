# board/models.py
from django.db import models


class Article(models.Model):
    # SQL) VARCHAR
    title = models.CharField(max_length=200)
    # SQL) TEXT
    content = models.TextField()