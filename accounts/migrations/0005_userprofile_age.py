# Generated by Django 3.1.4 on 2020-12-07 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_userprofile_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='age',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]
