# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-07 17:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parlamentares', '0011_auto_20160216_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='parlamentar',
            name='unidade_deliberativa',
            field=models.BooleanField(default=True, verbose_name='Unidade Deliberativa'),
            preserve_default=False,
        ),
    ]