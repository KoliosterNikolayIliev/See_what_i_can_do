# Generated by Django 3.1.4 on 2020-12-12 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_auto_20201211_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('Other', 'Other'), ('Nature', 'Nature'), ('Family', 'Family'), ('Animals', 'Animals'), ('Christmas', 'Christmas'), ('Easter', 'Easter'), ('City', 'City'), ('Fun', 'Fun')], default='Other', max_length=20),
        ),
    ]
