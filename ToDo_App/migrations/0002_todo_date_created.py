# Generated by Django 3.2.4 on 2021-11-11 12:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo_App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
