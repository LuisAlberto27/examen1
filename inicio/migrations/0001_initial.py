# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='modelo_Asistente',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('asistente_name', models.CharField(max_length=24)),
                ('asistente_apellido', models.CharField(max_length=24)),
                ('asistente_edad', models.FloatField()),
                ('asistente_matricula', models.CharField(max_length=24)),
            ],
        ),
    ]
