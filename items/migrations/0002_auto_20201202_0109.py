# Generated by Django 3.1.4 on 2020-12-01 23:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='art',
            new_name='item',
        ),
        migrations.RenameField(
            model_name='like',
            old_name='art',
            new_name='item',
        ),
    ]
