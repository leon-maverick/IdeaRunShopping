# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-07 10:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shopping', '0008_auto_20171205_1147'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotAvPro',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('Shopping.product',),
        ),
    ]