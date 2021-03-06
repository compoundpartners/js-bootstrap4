# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-14 13:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bootstrap4_grid', '0004_bootstrap4gridrow_layout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bootstrap4gridrow',
            name='layout',
            field=models.CharField(blank=True, choices=[('columns', 'Columns'), ('rows', 'Rows'), ('hero', 'Hero')], help_text='Select a layout', max_length=255, verbose_name='Layout'),
        ),
    ]
