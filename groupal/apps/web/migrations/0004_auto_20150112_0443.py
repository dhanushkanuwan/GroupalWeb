# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import groupal.apps.web.models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20150108_0218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactgroup',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to=groupal.apps.web.models.get_group_thumbnail_upload_path, blank=True),
        ),
    ]
