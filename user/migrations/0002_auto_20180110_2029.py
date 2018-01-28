# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='my_user',
            name='solve_Pwn',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='my_user',
            name='solve_Reverse',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='my_user',
            name='solve_Web',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='my_user',
            name='solve_sum',
            field=models.IntegerField(default=0),
        ),
    ]
