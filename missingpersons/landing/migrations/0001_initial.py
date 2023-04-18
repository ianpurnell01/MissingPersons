# Generated by Django 4.1.7 on 2023-04-18 21:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_at_missing', models.DateField(blank=True, default=datetime.datetime.today)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('missing_age', models.IntegerField()),
                ('city', models.CharField(max_length=45)),
                ('state', models.CharField(max_length=45)),
                ('gender', models.CharField(max_length=1)),
                ('race', models.CharField(max_length=1)),
            ],
        ),
    ]
