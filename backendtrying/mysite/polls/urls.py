from django.conf.urls import url

from . import views

app_name = "polls"
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="polls_index"),
    url(r'^credits/$', views.CreditsView.as_view(), name="credits"),
    url(r'^input_product/$', views.InputProductView.as_view(), name="input_product"),
    url(r'^your_recipe/$', views.YourRecipeView.as_view(), name="your_recipe"),
    url(r'^recipe_detail/(?P<pk>[0-9]+)/$', views.RecipeDetailView.as_view(), name="recipe_detail"),
]
