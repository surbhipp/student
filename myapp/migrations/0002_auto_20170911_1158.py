# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-11 06:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Address', models.CharField(max_length=30)),
                ('MobileNo', models.CharField(max_length=12)),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='select_team',
        ),
    ]