# Generated by Django 4.1.1 on 2022-09-22 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]
