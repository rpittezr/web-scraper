# Generated by Django 5.1.3 on 2024-11-11 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0002_alter_productscrapeevent_asin"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="_trigger_scrape",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="product",
            name="trigger_scrape",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="product",
            name="url",
            field=models.URLField(blank=True, null=True),
        ),
    ]