from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('lists', views.lists, name='lists'),
    path("recipes", views.recipes, name="recipes"),
    path("list/<int:list_id>", views.myList, name="list"),
    path('delete_list/<int:list_id>', views.delete_list, name='delete_list'),
    path("recipe/<int:recipe_id>", views.recipe, name="recipe"),
    path("search", views.search, name="search"),
    path("add_list_items/<str:list_id>", views.add_list_items, name="add_list_items"),
    path("suggestion_results/<str:category>", views.suggestion_recipes, name="suggestion_results"),
]