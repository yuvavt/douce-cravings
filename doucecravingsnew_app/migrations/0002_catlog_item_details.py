# Generated by Django 4.2.6 on 2023-10-25 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("doucecravingsnew_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Catlog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("item_name", models.CharField(max_length=200)),
                ("item_image", models.ImageField(upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="Item_Details",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("dessert_image", models.CharField(max_length=100)),
                ("dessert_title", models.CharField(max_length=200)),
                ("dessert_price", models.FloatField(default=0)),
                ("topping_name", models.TextField()),
                ("dessert_description", models.TextField()),
            ],
        ),
    ]