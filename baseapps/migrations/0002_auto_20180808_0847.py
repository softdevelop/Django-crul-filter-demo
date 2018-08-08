# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-08 08:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapps', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='phone',
            new_name='age',
        ),
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.AddField(
            model_name='user',
            name='sex',
            field=models.PositiveSmallIntegerField(choices=[(0, 'male'), (10, 'female')], default=0),
        ),
    ]