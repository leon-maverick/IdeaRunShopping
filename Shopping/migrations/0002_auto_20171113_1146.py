# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 11:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Shopping', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='person',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Done', 'Done'), ('Cancel', 'Cancel'), ('Handeling', 'Handeling')], max_length=1),
        ),
    ]
