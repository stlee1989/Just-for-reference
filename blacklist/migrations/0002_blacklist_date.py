# Generated by Django 2.2.5 on 2019-11-01 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blacklist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blacklist',
            name='date',
            field=models.CharField(default='-', max_length=12),
        ),
    ]
