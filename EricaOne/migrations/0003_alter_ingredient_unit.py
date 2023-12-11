# Generated by Django 4.2.7 on 2023-11-25 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EricaOne', '0002_ingredient_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='unit',
            field=models.CharField(choices=[('g', 'grams'), ('kg', 'kilograms'), ('ml', 'milliliters'), ('l', 'liters'), ('tsp', 'teaspoons'), ('tbsp', 'tablespoons'), ('cup', 'cups'), ('ea', 'each')], default='grams', max_length=5),
        ),
    ]
