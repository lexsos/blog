# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-20 04:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feed', '0002_auto_20161219_1544'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_red', models.BooleanField(default=False, verbose_name='post is red')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feed.Post', verbose_name='post')),
                ('subscriber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='subscriber')),
            ],
            options={
                'verbose_name_plural': 'feed items',
                'ordering': ('-post__create_at',),
                'verbose_name': 'feed item',
            },
        ),
        migrations.AlterUniqueTogether(
            name='feed',
            unique_together=set([('post', 'subscriber')]),
        ),
    ]