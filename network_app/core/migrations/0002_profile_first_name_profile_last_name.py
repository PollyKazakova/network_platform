# Generated by Django 4.2 on 2023-04-23 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="first_name",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="last_name",
            field=models.TextField(blank=True),
        ),
    ]