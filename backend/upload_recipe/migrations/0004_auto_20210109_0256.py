# Generated by Django 3.1.5 on 2021-01-09 07:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_recipe', '0003_auto_20210108_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fridgefood',
            name='days_to_expire',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='fridgefood',
            name='fridge_food_expire_date',
            field=models.DateField(default=datetime.datetime(2022, 1, 9, 2, 56, 21, 635125)),
        ),
        migrations.AlterField(
            model_name='fridgefood',
            name='fridge_food_name',
            field=models.CharField(default='FALSE_ENTRY', max_length=120),
        ),
    ]