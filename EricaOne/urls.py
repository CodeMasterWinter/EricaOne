from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('lists', views.lists, name='lists'),
    path("recipes/", views.recipes, name="recipes"),
    path("list/<int:list_id>", views.list, name="list"),
    path("recipe/<int:recipe_id>", views.recipe, name="recipe"),
    path("search_recipes", views.search_recipes, name="search_recipes"),
    path("suggestion_results/<str:category>", views.suggestion_recipes, name="suggestion_results"),
]