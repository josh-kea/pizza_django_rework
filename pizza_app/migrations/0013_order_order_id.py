# Generated by Django 3.1.3 on 2020-12-17 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_app', '0012_remove_order_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_id',
            field=models.IntegerField(default='0'),
        ),
    ]
