# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-03 14:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20170630_0213'),
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
            field=models.CharField(choices=[('Web', 'Web'), ('Others', 'Others'), ('App', 'App'), ('Design', 'Design')], default='App', max_length=200),
        ),
    ]
