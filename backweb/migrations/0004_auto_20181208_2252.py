# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-08 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backweb', '0003_article_keywords'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='icon',
            field=models.ImageField(null=True, upload_to='tb_article'),
        ),
    ]