# Generated by Django 4.2 on 2023-04-23 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_post"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.ImageField(blank=True, upload_to="post_images"),
        ),
    ]
