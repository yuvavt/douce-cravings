# Generated by Django 4.2.6 on 2023-11-14 00:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("doucecravingsnew_app", "0021_alter_list_of_items_date_modified"),
    ]

    operations = [
        migrations.AlterField(
            model_name="list_of_items",
            name="date_modified",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 11, 14, 0, 28, 39, 688501)
            ),
        ),
    ]
