# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-18 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=100)),
                ('phone_number', models.CharField(default='', max_length=15)),
                ('job_your_applying_for', models.CharField(default='', max_length=50)),
                ('years_experience', models.IntegerField()),
                ('work_experience', models.TextField()),
                ('about_you', models.TextField()),
            ],
        ),
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
