# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solos', '0004_solo_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solo',
            name='track',
            field=models.ForeignKey(to='albums.Track'),
        ),
    ]
