# Generated by Django 4.2 on 2024-06-24 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_rename_price_product_price_variation'),
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='variations',
            field=models.ManyToManyField(blank=True, to='store.variation'),
        ),
    ]