# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('data', models.TextField(verbose_name='Входящие параметры')),
                ('output', models.TextField(verbose_name='Ответ')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
