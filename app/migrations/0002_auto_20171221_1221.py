# Generated by Django 2.0 on 2017-12-21 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='application_secret',
            field=models.CharField(max_length=60, unique=True),
        ),
    ]
