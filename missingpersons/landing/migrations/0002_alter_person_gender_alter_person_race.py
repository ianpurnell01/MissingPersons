# Generated by Django 4.1.7 on 2023-04-19 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='person',
            name='race',
            field=models.CharField(max_length=30),
        ),
    ]
