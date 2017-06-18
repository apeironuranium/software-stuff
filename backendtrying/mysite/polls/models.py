import datetime

from django.db import models
from django.utils import timezone


class Recipe(models.Model):
    title = models.CharField(default="", max_length=50)
    recipe_text = models.CharField(max_length=400)
    pub_date = models.DateTimeField('date published')

    recipe_lines = models.ManyToManyField(
        'Food',
        through='RecipeLine',
        through_fields=('recipe', 'ingridient'),
    )

    def __str__(self):
        return self.recipe_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Food(models.Model):
    food_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.food_text


class RecipeLine(models.Model):
    recipe = models.ForeignKey(Recipe)
    ingridient = models.ForeignKey(Food)
    quantity = models.FloatField(default=0)
