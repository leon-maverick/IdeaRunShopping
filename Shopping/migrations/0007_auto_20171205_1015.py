# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 10:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shopping', '0006_auto_20171205_0926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, choices=[('P', 'Pending'), ('D', 'Done'), ('C', 'Cancel'), ('H', 'Handeling')], default='P', max_length=1),
        ),
    ]