# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-03 02:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20171101_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='tonggao',
            field=models.CharField(default='', max_length=100, verbose_name='课程公告'),
        ),
        migrations.AddField(
            model_name='video',
            name='videourl',
            field=models.CharField(default='', max_length=100, verbose_name='视频地址'),
        ),
    ]
