# Generated by Django 5.1.3 on 2024-11-15 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
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
                ("name", models.CharField(max_length=10)),
                ("major", models.CharField(max_length=20)),
                ("grade", models.IntegerField(default=1)),
                ("age", models.IntegerField(default=18)),
                ("gender", models.CharField(default="M", max_length=1)),
            ],
        ),
    ]
