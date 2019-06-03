# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-03 09:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bootstrap4_grid', '0006_auto_20190520_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bootstrap4gridrow',
            name='layout',
            field=models.CharField(blank=True, choices=[('no_vert_pad', 'No Vertical Padding'), ('center_feature', 'Center Feature')], help_text='Select a layout', max_length=255, verbose_name='Layout'),
        ),
    ]
