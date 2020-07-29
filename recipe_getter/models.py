from django.db import models
from django.contrib.postgres.fields import ArrayField


class RecipeData(models.Model):
    name = models.CharField(max_length=100, default="")
    meal_type = models.CharField(max_length=25, default="")
    address = models.TextField(default="")
    ingredients = ArrayField(models.CharField(max_length=90), default=list)
    image_url = models.TextField(default="")


class Ingredient(models.Model):
    name = models.CharField(max_length=60, default="")
