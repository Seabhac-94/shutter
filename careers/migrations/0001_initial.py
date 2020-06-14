# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-14 09:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobOpening',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(default='', max_length=100)),
                ('description', models.TextField()),
                ('closing_date', models.DateField()),
            ],
        ),
    ]
