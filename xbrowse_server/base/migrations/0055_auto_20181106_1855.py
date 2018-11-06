# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-06 18:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0054_familygroup_seqr_analysis_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individual',
            name='maternal_id',
            field=models.SlugField(blank=True, default=b'', max_length=140, null=True),
        ),
        migrations.AlterField(
            model_name='individual',
            name='paternal_id',
            field=models.SlugField(blank=True, default=b'', max_length=140, null=True),
        ),
    ]
