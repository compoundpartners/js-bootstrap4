# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-10 15:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bootstrap4_picture', '0005_bootstrap4picture_svg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bootstrap4picture',
            name='caption_text',
            field=models.TextField(blank=True, help_text='Provide a description, attribution, copyright or other information.', null=True, verbose_name='Caption text'),
        ),
        migrations.AlterField(
            model_name='bootstrap4picture',
            name='external_picture',
            field=models.URLField(blank=True, help_text='If provided, overrides the embedded image. Certain options such as cropping are not applicable to external images.', max_length=255, null=True, verbose_name='External image'),
        ),
        migrations.AlterField(
            model_name='bootstrap4picture',
            name='link_url',
            field=models.URLField(blank=True, help_text='Wraps the image in a link to an external URL.', max_length=2040, null=True, verbose_name='External URL'),
        ),
    ]
