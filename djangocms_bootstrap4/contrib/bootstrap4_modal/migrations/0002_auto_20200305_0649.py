# Generated by Django 2.2.10 on 2020-03-05 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bootstrap4_modal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bootstrap4modal',
            name='percentage_scrolled',
            field=models.CharField(blank=True, choices=[('', 'default'), ('5', '5%'), ('25', '25%'), ('50', '50%'), ('75', '75%'), ('90', '90%'), ('100', '100%')], default='', max_length=255, verbose_name='Percentage Scrolled'),
        ),
        migrations.AddField(
            model_name='bootstrap4modal',
            name='seconds_passed',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Seconds Passed'),
        ),
    ]
