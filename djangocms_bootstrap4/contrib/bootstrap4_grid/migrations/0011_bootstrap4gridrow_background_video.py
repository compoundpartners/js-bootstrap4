# Generated by Django 2.2.10 on 2020-06-04 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bootstrap4_grid', '0010_auto_20200521_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='bootstrap4gridrow',
            name='background_video',
            field=models.CharField(blank=True, max_length=255, verbose_name='Background Video'),
        ),
    ]
