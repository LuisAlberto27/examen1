# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='modelo_Ponente',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('ponente_name', models.CharField(max_length=24)),
                ('ponente_apellido', models.CharField(max_length=24)),
                ('ponente_edad', models.FloatField()),
                ('ponente_matricula', models.CharField(max_length=24)),
            ],
        ),
        migrations.CreateModel(
            name='modelo_Staff',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('staff_name', models.CharField(max_length=24)),
                ('staff_apellido', models.CharField(max_length=24)),
                ('staff_edad', models.FloatField()),
                ('staff_matricula', models.CharField(max_length=24)),
            ],
        ),
    ]
