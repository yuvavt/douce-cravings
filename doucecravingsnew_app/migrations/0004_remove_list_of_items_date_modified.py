# Generated by Django 4.2.6 on 2023-10-25 00:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("doucecravingsnew_app", "0003_best_sellers_home"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="list_of_items",
            name="date_modified",
        ),
    ]
