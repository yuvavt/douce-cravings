# Generated by Django 4.2.6 on 2023-10-25 03:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("doucecravingsnew_app", "0004_remove_list_of_items_date_modified"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Item_Details",
        ),
        migrations.AddField(
            model_name="list_of_items",
            name="date_modified",
            field=models.DateField(
                default=datetime.datetime(2023, 10, 25, 3, 6, 8, 698746)
            ),
        ),
        migrations.AddField(
            model_name="list_of_items",
            name="description",
            field=models.CharField(default=""),
        ),
        migrations.AddField(
            model_name="list_of_items",
            name="toppings",
            field=models.CharField(default=""),
        ),
    ]
