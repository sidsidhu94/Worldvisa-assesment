# Generated by Django 5.1 on 2024-08-27 10:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("categories", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
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
                (
                    "product_name",
                    models.CharField(
                        help_text="This will be displayed to user as-is",
                        max_length=150,
                        unique=True,
                        verbose_name="Product name",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        help_text="Few sentences that showcase the appeal of the product",
                        unique=True,
                        verbose_name="descriptive write-up",
                    ),
                ),
                (
                    "selling_price",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=10,
                        null=True,
                        verbose_name="price",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("edited_at", models.DateTimeField(auto_now=True)),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="products",
                        to="categories.category",
                    ),
                ),
            ],
            options={
                "verbose_name": "Product",
                "verbose_name_plural": "Products",
                "db_table": "product",
                "ordering": [],
            },
        ),
    ]
