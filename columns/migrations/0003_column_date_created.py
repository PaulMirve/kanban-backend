# Generated by Django 4.1.1 on 2022-09-27 01:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('columns', '0002_alter_column_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='column',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
