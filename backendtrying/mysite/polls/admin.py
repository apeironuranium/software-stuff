from django.contrib import admin
from polls.models import Recipe, Food, Choice
admin.site.register(Food)
admin.site.register(Choice)


class RecipeAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            'Date information',
            {
                'fields': ['pub_date'],
            },
        ),
        (
            'Recipe itself',
            {
                'fields': ['recipe_text'],
            },
        ),
    ]


admin.site.register(Recipe, RecipeAdmin)
