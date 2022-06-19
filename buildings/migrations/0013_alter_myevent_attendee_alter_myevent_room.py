# Generated by Django 4.0.5 on 2022-06-18 20:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('buildings', '0012_myevent_attendee_alter_myevent_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myevent',
            name='attendee',
            field=models.ManyToManyField(related_name='my_event_attendees', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='myevent',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_events_room', to='buildings.room'),
        ),
    ]
