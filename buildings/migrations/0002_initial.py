# Generated by Django 4.0.5 on 2022-06-17 06:42

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('buildings', '0001_initial'),
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('capacity', models.IntegerField(default=0)),
                ('permission_level', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('permission_company', multiselectfield.db.fields.MultiSelectField(choices=[(1, 'Pepsi'), (2, 'Coke')], max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('floor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='floor_rooms', to='buildings.floor')),
            ],
            options={
                'verbose_name_plural': 'Rooms',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='MyEvent',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='schedule.event')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events_room', to='buildings.room')),
            ],
            bases=('schedule.event',),
        ),
        migrations.AddField(
            model_name='floor',
            name='building',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='building_floor', to='buildings.building'),
        ),
        migrations.AddField(
            model_name='buildingimage',
            name='building',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='building_image', to='buildings.building'),
        ),
    ]