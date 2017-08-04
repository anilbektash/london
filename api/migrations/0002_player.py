# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-03 14:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True


    operations = [
        migrations.RunSQL(
            "CREATE INDEX player_id_index ON api_player USING gist(player_id);",
        ),
    ]

