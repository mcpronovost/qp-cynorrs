# Generated by Django 4.0.5 on 2022-07-25 22:16

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0008_qpworldstyle_app_header_txt_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='qpworldstyle',
            name='app_sidebar_txt',
            field=colorfield.fields.ColorField(default='#7a8489', image_field=None, max_length=18, samples=None, verbose_name='App Sidebar Text Colour'),
        ),
        migrations.AddField(
            model_name='qpworldstyle',
            name='default_bg',
            field=colorfield.fields.ColorField(default='#dbe0e2', image_field=None, max_length=18, samples=None, verbose_name='Default Background Colour'),
        ),
        migrations.AddField(
            model_name='qpworldstyle',
            name='primary',
            field=colorfield.fields.ColorField(default='#435259', image_field=None, max_length=18, samples=None, verbose_name='Primary Colour'),
        ),
    ]
