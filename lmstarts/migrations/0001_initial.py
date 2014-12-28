# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('active', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(verbose_name=b'Date created')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HostGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=60)),
                ('active', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(verbose_name=b'Date created')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='computer',
            name='host_group',
            field=models.ForeignKey(to='lmstarts.HostGroup'),
            preserve_default=True,
        ),
    ]
