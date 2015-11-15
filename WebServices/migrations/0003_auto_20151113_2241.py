# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebServices', '0002_auto_20151019_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='importance',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='text',
            name='title',
            field=models.TextField(choices=[(b'TI', b'title'), (b'AD', b'advertisement'), (b'AU', b'about us')]),
        ),
    ]
