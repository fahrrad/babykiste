# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadeau', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artikel',
            name='foto',
            field=models.ImageField(upload_to='', blank=True, verbose_name='media/img'),
        ),
    ]
