# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-07 21:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20170707_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='animation',
            field=models.CharField(choices=[('bounceInRight', 'bounceInRight'), ('bounceInUp', 'bounceInUp'), ('bounceInLeft', 'bounceInLeft'), ('bounceInDown', 'bounceInDown')], default='bounceInLeft', max_length=50),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='category',
            field=models.CharField(choices=[('Web', 'Web'), ('Design', 'Design'), ('Others', 'Others'), ('App', 'App')], default='App', max_length=200),
        ),
    ]
