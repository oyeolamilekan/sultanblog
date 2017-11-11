# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-11 10:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone_number', models.IntegerField()),
                ('email_field', models.EmailField(max_length=254)),
                ('createdate', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
