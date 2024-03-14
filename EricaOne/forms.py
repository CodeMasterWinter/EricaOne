from django import forms
from .models import Category


class NewDish(forms.Form):
    name = forms.CharField(label="Dish Name", max_length=255, required=True)
    prep_hours = forms.IntegerField(required=True)
    prep_minutes = forms.IntegerField(required=True)
    servings = forms.IntegerField(required=True)
    aliases = forms.JSONField(required=False)
    image = forms.ImageField(required=False)

    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )


class AddListItems(forms.Form):
    listItems = forms.CharField(widget=forms.Textarea, required=True)


class newList(forms.Form):
    title = forms.CharField(max_length=255, required=True)
    listItems = forms.CharField(widget=forms.Textarea, required=False)