# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-20 05:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0004_auto_20161220_0753'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='subscription',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='feed.Subscription', verbose_name='subscription item'),
        ),
    ]