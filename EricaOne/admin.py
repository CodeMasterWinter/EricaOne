from django.contrib import admin
from .models import Dish, Ingredient, Category, List, ListItem


class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 1


class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'prep_minutes', 'prep_hours', 'servings')
    inlines = [IngredientInline]


admin.site.register(Dish, DishAdmin)
admin.site.register(Ingredient)


class DishInline(admin.TabularInline):
    model = Dish.categories.through
    extra = 0  # Set to 0 to prevent an empty form for adding new dishes


class CategoryAdmin(admin.ModelAdmin):
    inlines = [DishInline]


class ListInline(admin.TabularInline):
    model = List.listItems.through
    extra = 0


class ListItemAdmin(admin.ModelAdmin):
    inlines = [ListInline]


admin.site.register(Category, CategoryAdmin)
admin.site.register(List)
admin.site.register(ListItem, ListItemAdmin)