# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='problem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('problem_name', models.CharField(max_length=20)),
                ('problem_describe', models.TextField()),
                ('problem_date', models.DateField()),
                ('problem_answer', models.CharField(max_length=50)),
            ],
        ),
    ]
