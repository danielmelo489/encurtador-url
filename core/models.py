from django.db import models

class UrlCurta(models.Model):
    urlOriginal = models.CharField(max_length=100)
    urlEncurtada = models.CharField(max_length=50)
