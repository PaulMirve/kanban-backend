# Generated by Django 4.1.1 on 2022-09-27 01:37

import columns.models
from django.db import migrations
import django_enumfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('columns', '0003_column_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='column',
            name='color',
            field=django_enumfield.db.fields.EnumField(default=0, enum=columns.models.ColorsEnum),
        ),
    ]
