# Generated by Django 4.0.5 on 2022-06-19 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0015_alter_myevent_attendee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myevent',
            old_name='attendee',
            new_name='attendees',
        ),
    ]
