# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-08 15:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backweb', '0004_auto_20181208_2252'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='type',
            new_name='category',
        ),
    ]
