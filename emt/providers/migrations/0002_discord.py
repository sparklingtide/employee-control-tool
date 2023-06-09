# Generated by Django 4.1.4 on 2022-12-26 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("providers", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Discord",
            fields=[
                (
                    "resource_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="providers.resource",
                    ),
                ),
                ("server_id", models.PositiveIntegerField()),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("providers.resource",),
        ),
    ]
