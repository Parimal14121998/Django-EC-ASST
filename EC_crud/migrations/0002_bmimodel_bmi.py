# Generated by Django 3.2 on 2023-03-04 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EC_crud', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bmimodel',
            name='bmi',
            field=models.FloatField(default=1),
        ),
    ]
