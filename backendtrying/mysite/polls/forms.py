from django import forms
from django_select2.forms import ModelSelect2TagWidget
from . import models


class FoodSelect2TagWidget(ModelSelect2TagWidget):
    search_fields = ['food_text__icontains']
    model = models.Food
    label = ''


class FoodModelSelect2TagWidgetForm(forms.ModelForm):
    class Meta:
        model = models.Food
        fields = ['food_text']
        widgets = {
            'food_text': FoodSelect2TagWidget,
        }
        labels = {
            'food_text': '',
        }
