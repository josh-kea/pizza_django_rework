# Generated by Django 3.1.3 on 2020-12-11 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_app', '0009_pizza_pizza_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza',
            name='pizza_id',
        ),
    ]
