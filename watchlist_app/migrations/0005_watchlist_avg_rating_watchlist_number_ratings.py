# Generated by Django 4.2.23 on 2025-06-13 12:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("watchlist_app", "0004_review_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="watchlist",
            name="avg_rating",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="watchlist",
            name="number_ratings",
            field=models.IntegerField(default=0),
        ),
    ]
