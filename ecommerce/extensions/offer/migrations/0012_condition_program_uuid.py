# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-05-08 18:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0011_auto_20170215_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='condition',
            name='program_uuid',
            field=models.UUIDField(blank=True, null=True, verbose_name='Program UUID'),
        ),
    ]
