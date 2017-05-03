# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-created',)},
        ),
        migrations.AddField(
            model_name='order',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 3, 21, 56, 59, 239882, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
