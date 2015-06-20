# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artikel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('naam', models.CharField(max_length=1024)),
                ('foto', models.ImageField(upload_to='', blank=True)),
                ('beschrijving', models.TextField()),
                ('beschikbaar_procent', models.IntegerField(default=100, verbose_name='% nog te koop')),
                ('totaal', models.DecimalField(max_digits=7, decimal_places=2, default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Cadeau',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('schenker', models.CharField(max_length=1024)),
                ('email_schenker', models.EmailField(max_length=254)),
                ('totaal', models.DecimalField(max_digits=7, decimal_places=2)),
                ('betaald', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CadeauItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('percent', models.IntegerField()),
                ('artikel', models.ForeignKey(to='cadeau.Artikel')),
                ('cadeau', models.ForeignKey(to='cadeau.Cadeau')),
            ],
        ),
        migrations.AddField(
            model_name='cadeau',
            name='cadeauItems',
            field=models.ManyToManyField(through='cadeau.CadeauItem', to='cadeau.Artikel'),
        ),
    ]
