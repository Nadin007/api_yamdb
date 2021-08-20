# Generated by Django 2.2.6 on 2021-08-17 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0011_auto_20210817_1742"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(
                default=True,
                help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                verbose_name="active",
            ),
        ),
    ]
