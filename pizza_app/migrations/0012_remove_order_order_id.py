# Generated by Django 3.1.3 on 2020-12-15 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_app', '0011_pizza_pizza_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_id',
        ),
    ]
