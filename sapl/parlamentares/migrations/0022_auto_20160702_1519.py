# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-02 18:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parlamentares', '0021_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessaolegislativa',
            name='legislatura',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parlamentares.Legislatura', verbose_name='Legislatura'),
        ),
    ]
