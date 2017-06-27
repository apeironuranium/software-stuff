import datetime

from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError


class Recipe(models.Model):  # модели в базе данных
    title = models.CharField(default="", max_length=50)  # столбцы в таблице в базе
    recipe_text = models.TextField(max_length=1500)
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

    def clean(self):
        if self.quantity <= 0:
            raise ValidationError("Minimum no. of ingridients should be less or equal than maximum")
        return super(quantity, self).clean()