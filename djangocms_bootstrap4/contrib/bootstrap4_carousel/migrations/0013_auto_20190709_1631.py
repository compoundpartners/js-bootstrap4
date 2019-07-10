# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-09 16:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import djangocms_link.validators
import filer.fields.file
import js_color_picker.fields


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0011_auto_20190418_0137'),
        ('bootstrap4_carousel', '0012_auto_20190701_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='bootstrap4carouselslide',
            name='file_link',
            field=filer.fields.file.FilerFileField(blank=True, help_text='If provided links a file from the filer app.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='filer.File', verbose_name='File link'),
        ),
        migrations.AlterField(
            model_name='bootstrap4carouselslide',
            name='background_color',
            field=js_color_picker.fields.RGBColorField(blank=True, colors={'#0067A5': 'Dark Blue', '#009fe3': 'Blue', '#0A80C7': 'Medium Blue', '#2D9CDE': 'Light Blue', '#34BCE1': 'Sky', '#545454': 'Dark Grey', '#68C0B5': 'Teal', '#69CCE7': 'Light Sky', '#6d6d6d': 'Grey', '#8FD1E9': 'Very Light Sky', '#96D0C9': 'Light Teal', '#999': 'Light Grey', '#9B8DA5': 'Purple', '#B8AEBF': 'Light Purple', '#BBE9E4': 'Very Light Teal', '#C6BDCB': 'Very Light Purple', '#F2F2F2': 'Very Light Grey', '#F8EB91': 'Yellow', '#FEF4B4': 'Light Yellow', '#FF0000': 'White'}, mode='both', null=True, verbose_name='Background Color'),
        ),
        migrations.AlterField(
            model_name='bootstrap4carouselslide',
            name='external_link',
            field=models.CharField(blank=True, help_text='Provide a link to an external source.', max_length=2040, validators=[djangocms_link.validators.IntranetURLValidator(intranet_host_re=None)], verbose_name='External link'),
        ),
    ]