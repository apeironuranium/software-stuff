from django.test import TestCase
from polls.models import Food
from polls.models import Recipe
from polls.models import RecipeLine

class TestFoodString(TestCase):
    def setUp(self):
        Food.objects.create(food_text = "Valeriia", pub_date = "1993-06-29")

    def test_str_repr(self):
        title = "Valeriia"
        food_text = Food.objects.get(food_text=title)
        self.assertEqual(str(food_text), title)


class TestRecipeString(TestCase):
   def setUp(self):
       RecipeLine.objects.create(ingridient = "Oguretc")

   def test_str_repr(self):
       title = "Oguretc"
       ingridient = Food.objects.get(food_text=title)
       self.assertEqual(str(ingridient), title)