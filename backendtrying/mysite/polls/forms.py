from django import forms
from . import models


class ProductSelectionForm(forms.ModelForm):
    class Meta:
        model = models.Food
        fields = []

    def __init__(self, *args, **kwargs):
        super(ProductSelectionForm, self).__init__(*args, **kwargs)

        self.fields['food_list'] = forms.ModelMultipleChoiceField(
            widget=forms.SelectMultiple,
            queryset=models.Food.objects.all(),
        )
