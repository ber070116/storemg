from django.db import models
from apps.user.models import User


class Articles(models.Model):
    """
        Articles
    """
    name = models.CharField('name article', max_length=15)
    quantity = models.CharField('quantity from articles', max_length=15)
    description = models.CharField(max_length=200, unique=True)


class Showcases(models.Model):
    """
        Showcases that have the stores
    """
    name = models.CharField('name from showcase', max_length=15)
    articles = models.ForeignKey(Articles, on_delete=models.CASCADE)


class Stores(models.Model):
    """
        Class for the stores
    """
    name = models.CharField('name from store', max_length=15)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    showcases = models.ForeignKey(Showcases, on_delete=models.CASCADE)
