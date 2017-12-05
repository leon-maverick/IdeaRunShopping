# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 09:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Shopping', '0005_auto_20171114_0833'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=50, verbose_name='related category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='Shopping.Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pic',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]