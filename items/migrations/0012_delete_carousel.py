# Generated by Django 3.1.4 on 2020-12-04 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0011_remove_carousel_item'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Carousel',
        ),
    ]