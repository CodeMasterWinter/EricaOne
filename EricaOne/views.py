from random import sample
from .forms import NewDish
from .models import Dish, Category
from EricaOne.Scripts.Ericadatetime import DateTime
from django.shortcuts import render, redirect, reverse


def index(request):

    if int(DateTime().hour()) > 16:
        meal_time = "Dinner"
    elif int(DateTime().hour()) > 10:
        meal_time = "Lunch"
    else:
        meal_time = "Breakfast"

    context = {
        'meal_time': meal_time,
    }

    return render(request, 'EricaOne/index.html', context)


def recipes(request):

    all_categories = Category.objects.all()
    categories = sample(list(all_categories), 4)
    all_dishes = Dish.objects.all()
    dishes = []


    for category in categories:
        dishcount = 0
        for dish in all_dishes:
            if category in dish.get_categories:
                dishes.append(dish)
                dishcount += 1
                if dishcount == 4:
                    break
        if len(dishes) == 16:
            break

    if request.method == "POST":
        dishForm = NewDish(request.POST)
        if dishForm.is_valid():
            dish = Dish(name=dishForm.cleaned_data["name"],
                        prep_hours=dishForm.cleaned_data["prep_hours"],
                        prep_minutes=dishForm.cleaned_data["prep_minutes"],
                        servings=dishForm.cleaned_data["servings"])
            if dishForm.cleaned_data["aliases"] is not None:
                dish.aliases = dishForm.cleaned_data["aliases"]

            dish.image = request.FILES.get("image")
            dish.save()
            return redirect(reverse(f"recipe", args=[dish.id]))
    else:
        dishForm = NewDish()

    context = {
        'dishForm': dishForm,
        'categories': categories,
        'dishes': dishes,
    }

    return render(request, 'EricaOne/recipes.html', context)


def search_recipes(request):

    if request.method == "POST":
        searchbar = request.POST["searchbar"]
        results = Dish.objects.filter(name__contains=searchbar)

        context = {
            'searchbar': searchbar,
            'results': results,
        }

        return render(request, 'EricaOne/search_recipe.html', context)
    else:
        context = {

        }

        return render(request, 'EricaOne/search_recipe.html', context)


def recipe(request, recipe_id):

    recipe = Dish.objects.get(id=recipe_id)

    context = {
        'recipe': recipe,
    }

    return render(request, 'EricaOne/recipe.html', context)