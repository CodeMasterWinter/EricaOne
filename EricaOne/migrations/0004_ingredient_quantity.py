# Generated by Django 4.2.7 on 2023-11-25 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EricaOne', '0003_alter_ingredient_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='quantity',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5),
        ),
    ]
