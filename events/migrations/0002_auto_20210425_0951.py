# Generated by Django 3.2 on 2021-04-25 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='end',
            new_name='end_time',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='start',
            new_name='start_time',
        ),
    ]
