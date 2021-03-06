# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-04 09:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bootstrap4_grid', '0007_auto_20190603_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bootstrap4gridcolumn',
            name='layout',
            field=models.CharField(blank=True, choices=[('title_yellow_big', 'Title - Yellow Big')], help_text='Select a layout', max_length=255, verbose_name='Layout'),
        ),
        migrations.AlterField(
            model_name='bootstrap4gridrow',
            name='layout',
            field=models.CharField(blank=True, choices=[('banner_dark', 'Banner - Dark'), ('banner_yellow', 'Banner - Yellow'), ('title_yellow_italic', 'Title - Yellow Italic'), ('title_yellow_regular', 'Title - Yellow Regular'), ('title_yellow_caps', 'Title - Yellow Caps'), ('title_dark_italic', 'Title - Dark Italic'), ('title_dark_regular', 'Title - Dark Regular'), ('title_dark_caps', 'Title - Dark Caps'), ('title_color_bar', 'Title - Color Bar')], help_text='Select a layout', max_length=255, verbose_name='Layout'),
        ),
    ]
