# Generated by Django 2.2.12 on 2020-10-05 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bootstrap4_grid', '0012_auto_20200608_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='bootstrap4gridrow',
            name='lg_hide',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='bootstrap4gridrow',
            name='md_hide',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='bootstrap4gridrow',
            name='sm_hide',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='bootstrap4gridrow',
            name='xl_hide',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='bootstrap4gridrow',
            name='xs_hide',
            field=models.BooleanField(default=False),
        ),
    ]