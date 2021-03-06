# Generated by Django 4.0.5 on 2022-07-18 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('forum', '0001_initial'),
        ('player', '0001_initial'),
        ('world', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='qpforummessage',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='messages', to='player.qpplayerhero', verbose_name='Author'),
        ),
        migrations.AddField(
            model_name='qpforummessage',
            name='chapter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='forum.qpforumchapter', verbose_name='Chapter'),
        ),
        migrations.AddField(
            model_name='qpforumchapter',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='chapters', to='player.qpplayerhero', verbose_name='Author'),
        ),
        migrations.AddField(
            model_name='qpforumchapter',
            name='last_message',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lastmessage_chapter', to='forum.qpforummessage', verbose_name='Last Message'),
        ),
        migrations.AddField(
            model_name='qpforumchapter',
            name='sector',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='chapters', to='forum.qpforumsector', verbose_name='Sector'),
        ),
        migrations.AddField(
            model_name='qpforumchapter',
            name='territory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='chapters', to='forum.qpforumterritory', verbose_name='Territory'),
        ),
        migrations.AddField(
            model_name='qpforum',
            name='administrators',
            field=models.ManyToManyField(blank=True, related_name='admin_forums', to='player.qpplayer', verbose_name='Administrators'),
        ),
        migrations.AddField(
            model_name='qpforum',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='creator_forums', to='player.qpplayer', verbose_name='Creator'),
        ),
        migrations.AddField(
            model_name='qpforum',
            name='moderators',
            field=models.ManyToManyField(blank=True, related_name='modo_forums', to='player.qpplayer', verbose_name='Moderators'),
        ),
        migrations.AddField(
            model_name='qpforum',
            name='world',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='forum', to='world.qpworld', verbose_name='World'),
        ),
    ]
