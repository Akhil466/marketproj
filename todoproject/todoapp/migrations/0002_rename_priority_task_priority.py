# Generated by Django 3.2.13 on 2022-05-03 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='Priority',
            new_name='priority',
        ),
    ]
