# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 11:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_profile_owner_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='AskJola',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email_state', models.EmailField(max_length=254)),
                ('body', models.TextField()),
            ],
        ),
    ]
