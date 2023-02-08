from django.db import models
from django.template.defaultfilters import slugify


class Phone(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    image = models.ImageField(null=True)
    release_date = models.DateField('%Y-%m-%d', null=True)
    lte_exists = models.BooleanField(null=True)
    slug = models.SlugField(max_length = 55)

