# Generated by Django 4.0.5 on 2022-07-20 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0003_qpplayercompanion_is_valid_qpplayerhero_is_valid'),
    ]

    operations = [
        migrations.AddField(
            model_name='qpplayer',
            name='limits_create_heros',
            field=models.PositiveSmallIntegerField(default=10, verbose_name='Hero Creation Limit'),
        ),
        migrations.AddField(
            model_name='qpplayer',
            name='limits_create_worlds',
            field=models.PositiveSmallIntegerField(default=2, verbose_name='World Creation Limit'),
        ),
        migrations.AlterField(
            model_name='qpplayer',
            name='settings_perpage_chapters',
            field=models.PositiveSmallIntegerField(default=12, verbose_name='Chapitres per page'),
        ),
        migrations.AlterField(
            model_name='qpplayer',
            name='settings_perpage_messages',
            field=models.PositiveSmallIntegerField(default=20, verbose_name='Messages per page'),
        ),
    ]
