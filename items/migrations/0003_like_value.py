# Generated by Django 3.1.4 on 2020-12-01 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_auto_20201202_0109'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='value',
            field=models.CharField(default=1, max_length=2),
            preserve_default=False,
        ),
    ]
