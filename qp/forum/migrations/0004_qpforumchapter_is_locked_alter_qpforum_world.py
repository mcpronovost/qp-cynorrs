# Generated by Django 4.0.5 on 2022-07-24 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0005_qpworld_description'),
        ('forum', '0003_remove_qpforum_administrators_remove_qpforum_creator_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='qpforumchapter',
            name='is_locked',
            field=models.BooleanField(default=False, verbose_name='Locked'),
        ),
        migrations.AlterField(
            model_name='qpforum',
            name='world',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='forum', to='world.qpworld', verbose_name='World'),
        ),
    ]
