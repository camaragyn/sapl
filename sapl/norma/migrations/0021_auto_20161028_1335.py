# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-28 13:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('norma', '0020_auto_20161028_1335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='normajuridica',
            name='assuntos',
        ),
        migrations.AddField(
            model_name='normajuridica',
            name='assuntos',
            field=models.ManyToManyField(blank=True, to='norma.AssuntoNorma', verbose_name='Assuntos'),
        ),
    ]
