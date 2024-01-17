from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path("recipes/", views.recipes, name="recipes"),
    path("recipe/<int:recipe_id>", views.recipe, name="recipe"),
    path("search_recipes", views.search_recipes, name="search_recipes"),
    path("suggestion_results/<str:category>", views.suggestion_recipes, name="suggestion_results"),
]