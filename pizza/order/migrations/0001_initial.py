# Generated by Django 3.2.8 on 2024-08-08 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pizza', '0002_auto_20240808_1734'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addres', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('pizza_order', models.ManyToManyField(to='pizza.PizzaModel')),
            ],
        ),
    ]
