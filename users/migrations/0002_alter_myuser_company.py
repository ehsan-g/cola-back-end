# Generated by Django 4.0.5 on 2022-06-15 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='company',
            field=models.IntegerField(choices=[(0, '-'), (1, 'Pepsi'), (2, 'Coke')], default=0),
        ),
    ]