from django.contrib import admin
from .models import Recipe, RecipeLine, Food
admin.site.register(Food)


class RecipeLineInline(admin.StackedInline):
    model = RecipeLine


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
                'fields': ['title', 'recipe_text'],
            },
        ),
    ]
    list_display = ("title",)
    list_filter = ['pub_date']
    inlines = [RecipeLineInline]

admin.site.register(Recipe, RecipeAdmin)
