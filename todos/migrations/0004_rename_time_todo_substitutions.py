# Generated by Django 4.2.7 on 2023-11-04 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0003_todo_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='time',
            new_name='substitutions',
        ),
    ]
