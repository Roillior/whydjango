# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 19:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('referral_module', '0004_auto_20171102_1938'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userreferrerstats',
            options={'verbose_name': 'User referrer stats', 'verbose_name_plural': 'User referrer stats'},
        ),
        migrations.AddField(
            model_name='userreferrer',
            name='reward',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=10),
        ),
    ]
