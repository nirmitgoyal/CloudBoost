# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-20 10:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elasticsearch_and_redis_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='book_id',
        ),
    ]
