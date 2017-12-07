# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-06 07:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('blogId', models.AutoField(primary_key=True, serialize=False)),
                ('blogContent', models.CharField(max_length=140)),
                ('bloggedDate', models.DateField()),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
