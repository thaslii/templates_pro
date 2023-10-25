from django.db import models

class Article(models.Model):
    img = models.ImageField(upload_to='pics')
