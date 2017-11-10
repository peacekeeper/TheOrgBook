# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-09 21:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20171108_0936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='verifiableOrgId',
        ),
        migrations.AlterField(
            model_name='locationorg',
            name='doingBusinessAsId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doingBusinessAsLocations', to='api.DoingBusinessAs'),
        ),
        migrations.AlterField(
            model_name='locationorg',
            name='verifiableOrgId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='verifiableOrgLocations', to='api.VerifiableOrg'),
        ),
    ]
