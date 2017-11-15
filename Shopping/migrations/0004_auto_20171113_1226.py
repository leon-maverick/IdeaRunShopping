# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 12:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shopping', '0003_auto_20171113_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('P', 'Pending'), ('D', 'Done'), ('C', 'Cancel'), ('H', 'Handeling')], default='Pending', max_length=1),
        ),
    ]