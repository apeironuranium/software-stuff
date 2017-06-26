from django.views import generic
from django.shortcuts import render
from . import models
from .forms import FoodModelSelect2TagWidgetForm


class IndexView(generic.TemplateView):
    template_name = "polls/index.html"


class CreditsView(generic.TemplateView):
    template_name = "polls/credits.html"


class InputProductView(generic.FormView):
    template_name = "polls/input_product.html"
    form_class = FoodModelSelect2TagWidgetForm


class YourRecipeView(generic.TemplateView):
    template_name = "polls/your_recipe.html"

    def get(self, request, *args):
        food_list = request.GET.getlist('food_text')
        food_ids = []
        for item in food_list:
            try:
                food_ids.append(int(item))
            except ValueError:
                pass
        res = models.Recipe.objects.filter(recipe_lines__in=food_ids).distinct()
        # Old algorithm for strict search
        # vals = []
        # food_ids = set(food_ids)
        # for item in res.all():
        #     food_set = set()
        #     for i in item.recipe_lines.values('id'):
        #         food_set.add(i['id'])
        #     if food_ids.issuperset(food_set):
        #         vals.append(item)
        return render(request, self.template_name, {'food_ids': res.all()})


class RecipeDetailView(generic.DetailView):
    model = models.Recipe
    template_name = "polls/recipe_detail.html"

    def get_context_data(self, **kwargs):
        context = super(RecipeDetailView, self).get_context_data(**kwargs)
        recipe_obj = context.get('object')
        recipe_lines = models.RecipeLine.objects.filter(recipe=recipe_obj).all()
        context['recipe_lines'] = recipe_lines
        return context
