# Generated by Django 2.0 on 2017-12-21 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20171221_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='logo',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='application',
            name='application_secret',
            field=models.CharField(blank=True, max_length=60, unique=True),
        ),
    ]