# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-13 16:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bootstrap4_cta', '0003_bootstrap4cta_layout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bootstrap4cta',
            name='layout',
            field=models.CharField(blank=True, choices=[('yellow_corner', 'Yellow Corner'), ('dark_corner_icon', 'Dark Corner Icon'), ('grey_corner', 'Grey Corner')], help_text='Select a layout', max_length=255, verbose_name='Layout'),
        ),
    ]