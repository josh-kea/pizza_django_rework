# Generated by Django 3.1.3 on 2020-12-17 22:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_app', '0013_order_order_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_id',
        ),
    ]
