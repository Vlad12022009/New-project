# Generated by Django 3.2.8 on 2024-08-22 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToppingsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Toppings',
                'verbose_name_plural': 'Toppings',
            },
        ),
        migrations.CreateModel(
            name='PizzaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('name_slug', models.SlugField(blank=True, null=True)),
                ('toppings', models.ManyToManyField(to='pizza.ToppingsModel', verbose_name='toppings')),
            ],
            options={
                'verbose_name': 'My pizza recipes',
                'verbose_name_plural': 'Pizza recipes',
            },
        ),
    ]
