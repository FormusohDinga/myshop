# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20170503_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated',
            field=models.DateTimeField(),
        ),
    ]
