# Generated by Django 4.2.6 on 2024-03-06 07:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20231209_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='dob',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
