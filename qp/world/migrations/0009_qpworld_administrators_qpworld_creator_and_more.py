# Generated by Django 4.0.5 on 2022-07-16 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0003_qpplayer_avatar_qpplayercompanion_avatar_and_more'),
        ('world', '0008_alter_qpworldchapter_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='qpworld',
            name='administrators',
            field=models.ManyToManyField(blank=True, related_name='admin_worlds', to='player.qpplayer', verbose_name='Administrators'),
        ),
        migrations.AddField(
            model_name='qpworld',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='creator_worlds', to='player.qpplayer', verbose_name='Creator'),
        ),
        migrations.AddField(
            model_name='qpworld',
            name='moderators',
            field=models.ManyToManyField(blank=True, related_name='modo_worlds', to='player.qpplayer', verbose_name='Moderators'),
        ),
    ]