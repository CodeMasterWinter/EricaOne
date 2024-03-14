from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_delete


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Dish(models.Model):
    name = models.CharField(max_length=255)
    prep_minutes = models.IntegerField(default=0)
    prep_hours = models.IntegerField(default=0)
    servings = models.IntegerField()
    aliases = models.JSONField(blank=True, null=True)
    categories = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='dish_images/', blank=True, null=True, max_length=255)

    def __str__(self):
        return self.name

    def get_prep_time(self):
        return f"{self.prep_hours}:{self.prep_minutes}"

    @property
    def get_categories(self):
        return list(category for category in self.categories.all())

    class Meta:
        verbose_name_plural = "Dishes"


class Ingredient(models.Model):

    units = [
        ('g', 'grams'),
        ('kg', 'kilograms'),
        ('ml', 'milliliters'),
        ('l', 'liters'),
        ('tsp', 'teaspoons'),
        ('tbsp', 'tablespoons'),
        ('cup', 'cups'),
        ('ea', 'each'),
    ]
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='ingredients')
    name = models.CharField(max_length=255)
    quantity = models.DecimalField(max_digits=5, decimal_places=2, default=1)
    unit = models.CharField(max_length=5, choices=units, default='grams')

    def __str__(self):
        if self.unit == 'ea':
            return f"{self.quantity} {self.name}"
        else:
            return f"{self.quantity} {self.unit} {self.name}"


class ListItem(models.Model):

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class List(models.Model):

    title = models.CharField(max_length=255)
    listItems = models.ManyToManyField(ListItem, blank=True)

    def __str__(self):
        return self.title
