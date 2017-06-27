from django.test import TestCase
from polls.models import Food, Recipe, RecipeLine
from django.core.exceptions import ValidationError

class TestFoodString(TestCase):
    def setUp(self):
        Food.objects.create(food_text = "Valeriia", pub_date = "1993-06-29")
        Recipe.objects.create(title="title", recipe_text="text",  pub_date = "1993-06-29")

    def test_str_repr(self):
        title = "Valeriia"
        food_text = Food.objects.get(food_text=title)
        self.assertEqual(str(food_text), title)


    def test_number_of_ingridients(self):
        recipe = Recipe.objects.get(pk=1)
        food = Food.objects.get(pk=1)
        self.assertRaises(ValidationError, RecipeLine.objects.create(
            recipe=recipe,
            ingridient=food,
            quantity = -1
        ).clean)
