# Generated by Django 4.2.6 on 2023-11-14 01:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("doucecravingsnew_app", "0025_alter_list_of_items_date_modified"),
    ]

    operations = [
        migrations.AlterField(
            model_name="list_of_items",
            name="date_modified",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 11, 14, 1, 16, 40, 204558)
            ),
        ),
    ]
