# Generated by Django 4.1.1 on 2022-09-27 01:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0003_alter_board_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
