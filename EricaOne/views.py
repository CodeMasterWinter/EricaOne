from random import sample
from .forms import NewDish, newList
from .models import Dish, Category, List, ListItem
from EricaOne.Scripts.Ericadatetime import DateTime
from django.shortcuts import render, redirect, reverse


def index(request):

    if int(DateTime().hour()) > 16:
        meal_time = "Dinner"
    elif int(DateTime().hour()) > 10:
        meal_time = "Lunch"
    else:
        meal_time = "Breakfast"

    all_dishes = Dish.objects.all()
    category = Category.objects.get(name=meal_time)
    dish_filter = all_dishes.filter(categories=category)
    dishes = sample(list(dish_filter), 2)

    context = {
        'meal_time': meal_time,
        'dishes': dishes,
        'page_title': 'Home'
    }

    return render(request, 'EricaOne/index.html', context)


def recipes(request):

    all_categories = Category.objects.all()
    categories = sample(list(all_categories), 4)
    all_dishes = Dish.objects.all()

    results = []

    for category in categories:
        dishes_in_category = list(all_dishes.filter(categories=category))
        random_dishes = sample(dishes_in_category, min(4, len(dishes_in_category)))

        category_data = {
            'category': category,
            'dishes': random_dishes,
        }

        results.append(category_data)
        if len(results) == 4:
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
        'results': results,
        'page_title': 'Recipes'
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


def suggestion_recipes(request, category):

    category = Category.objects.get(name=category)
    results = Dish.objects.filter(categories=category)

    context = {
        'category': category,
        'results': results,
    }

    return render(request, 'EricaOne/search_recipe.html', context)


def recipe(request, recipe_id):

    recipe = Dish.objects.get(id=recipe_id)

    context = {
        'recipe': recipe,
    }

    return render(request, 'EricaOne/recipe.html', context)


def lists(request):

    my_lists = List.objects.all()

    if request.method == "POST":
        listForm = newList(request.POST)
        if listForm.is_valid():
            title = listForm.cleaned_data["title"],
            title = list(title)
            newlist = List(title=title[0])
            list_items = listForm.cleaned_data["listItems"]
            newlist.save()

            list_items_list = list_items.split(", ")
            for listitem in list_items_list:
                newlistitem = ListItem(name=listitem)
                newlistitem.save()
                newlist.listItems.add(newlistitem)

            newlist.save()
            return redirect('lists')
    else:
        listForm = newList()

    context = {
        'lists': my_lists,
        'listForm': listForm,
        'page_title': "Lists",
    }

    return render(request, 'EricaOne/lists.html', context)


def myList(request, list_id):

    the_list = List.objects.get(id=list_id)

    context = {
        'list': the_list,
        'page_title': "Lists",
    }

    return render(request, 'EricaOne/list.html', context)
