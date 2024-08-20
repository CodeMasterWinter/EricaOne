from random import sample
from django.http import Http404
from .forms import NewDish, newList, AddListItems
from .models import Dish, Category, List, ListItem
from EricaOne.Scripts.Ericadatetime import DateTime
from django.shortcuts import render, redirect, reverse, get_object_or_404


def index(request):

    if int(DateTime().hour()) > 16:
        meal_time = "Dinner"
    elif int(DateTime().hour()) > 10:
        meal_time = "Lunch"
    else:
        meal_time = "Breakfast"

    # all_dishes = Dish.objects.all()
    # category = Category.objects.get(name=meal_time)
    # dish_filter = all_dishes.filter(categories=category)
    # dishes = sample(list(dish_filter), 2)

    context = {
        'meal_time': meal_time,
        # 'dishes': dishes,
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


def search(request):

    if request.method == "POST":
        searchbar = request.POST["searchbar"]

        search_model = request.POST["search_model"]

        if search_model == "dish":
            if not searchbar == "":
                results = Dish.objects.filter(name__contains=searchbar)
            else:
                results = []
                
        elif search_model == "list":
            if not searchbar == "":
                results = List.objects.filter(title__contains=searchbar)
            else:
                results = []

        context = {
            'searchbar': searchbar,
            'search_model': search_model,
            'results': results,
        }

    else:
        context = {

        }

    return render(request, 'EricaOne/search.html', context)


def suggestion_recipes(request, category):

    category = Category.objects.get(name=category)
    results = Dish.objects.filter(categories=category)

    context = {
        'category': category,
        'results': results,
    }

    return render(request, 'EricaOne/search.html', context)


def recipe(request, recipe_id):

    recipe = Dish.objects.get(id=recipe_id)

    context = {
        'recipe': recipe,
    }

    return render(request, 'EricaOne/recipe.html', context)


def check_monthly_budget():
    month = DateTime().month()
    try:
        target = List.objects.get(title__contains="Monthly budget")
        if target.title.lower() == f"monthly budget - {month.lower()}":
                pass
        else:
            target.delete()
            budget_list = List(title=f"Monthly budget - {month}")
            budget_list.save()
    except List.DoesNotExist:
            budget_list = List(title=f"Monthly budget - {month}")
            budget_list.save()


def lists(request):

    check_monthly_budget()
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
        'addListItems': AddListItems,
    }

    return render(request, 'EricaOne/lists.html', context)


def add_list_items(request, list_id):
    if request.method == "POST":

        target_list = get_object_or_404(List, id=list_id)
        newlistitems = AddListItems(request.POST)

        if newlistitems.is_valid():

            list_items = newlistitems.cleaned_data["listItems"].split(", ")
            for listitem in list_items:
                newlistitem = ListItem.objects.create(name=listitem)
                newlistitem.save()
                target_list.listItems.add(newlistitem)
            target_list.save()

        return redirect('lists')


def delete_list(request, list_id):
    list_to_delete = get_object_or_404(List, id=list_id)
    list_to_delete.delete()
    return redirect('lists')


def myList(request, list_id):

    the_list = List.objects.get(id=list_id)

    context = {
        'list': the_list,
        'page_title': "Lists",
    }

    return render(request, 'EricaOne/list.html', context)
