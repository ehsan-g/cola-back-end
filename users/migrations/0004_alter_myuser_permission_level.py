# Generated by Django 4.0.5 on 2022-06-16 19:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_level_myuser_permission_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='permission_level',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
    ]
