# Generated by Django 4.0.5 on 2022-06-13 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='level',
            field=models.IntegerField(default=0),
        ),
    ]
