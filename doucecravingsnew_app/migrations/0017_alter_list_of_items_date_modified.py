# Generated by Django 4.2.6 on 2023-11-09 22:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("doucecravingsnew_app", "0016_alter_list_of_items_date_modified"),
    ]

    operations = [
        migrations.AlterField(
            model_name="list_of_items",
            name="date_modified",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 11, 9, 22, 19, 57, 333366)
            ),
        ),
    ]
