# Generated by Django 4.0.5 on 2022-07-20 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0004_alter_qpworld_visibility'),
    ]

    operations = [
        migrations.AddField(
            model_name='qpworld',
            name='description',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Description'),
        ),
    ]