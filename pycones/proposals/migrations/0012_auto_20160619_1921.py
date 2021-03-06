# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-19 17:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0011_auto_20150918_1221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proposal',
            name='paper',
        ),
        migrations.AddField(
            model_name='proposal',
            name='duration',
            field=models.PositiveIntegerField(choices=[(15, '15 minutos'), (30, '30 minutos')], default=30),
        ),
        migrations.AddField(
            model_name='proposal',
            name='language',
            field=models.CharField(choices=[('es', 'Español'), ('en', 'Inglés')], default='es', max_length=2),
        ),
    ]
