# Generated by Django 4.2.7 on 2023-11-25 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('prep_time', models.DurationField()),
                ('servings', models.IntegerField()),
                ('aliases', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='EricaOne.dish')),
            ],
        ),
    ]
