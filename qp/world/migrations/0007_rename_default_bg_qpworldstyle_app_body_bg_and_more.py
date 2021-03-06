# Generated by Django 4.0.5 on 2022-07-25 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0006_qpworldstyle'),
    ]

    operations = [
        migrations.RenameField(
            model_name='qpworldstyle',
            old_name='default_bg',
            new_name='app_body_bg',
        ),
        migrations.RenameField(
            model_name='qpworldstyle',
            old_name='default_txt',
            new_name='app_body_txt',
        ),
        migrations.AlterField(
            model_name='qpworldstyle',
            name='stylesheet',
            field=models.TextField(blank=True, default='', verbose_name='Custom Stylesheet'),
        ),
    ]
