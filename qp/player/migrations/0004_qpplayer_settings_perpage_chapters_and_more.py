# Generated by Django 4.0.5 on 2022-07-17 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0003_qpplayer_avatar_qpplayercompanion_avatar_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='qpplayer',
            name='settings_perpage_chapters',
            field=models.PositiveSmallIntegerField(default=20, verbose_name='Chapitres par page'),
        ),
        migrations.AddField(
            model_name='qpplayer',
            name='settings_perpage_messages',
            field=models.PositiveSmallIntegerField(default=20, verbose_name='Messages par page'),
        ),
    ]
