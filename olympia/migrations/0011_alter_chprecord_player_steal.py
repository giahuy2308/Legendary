# Generated by Django 5.2.2 on 2025-06-14 16:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olympia', '0010_alter_vcnvrecord_player_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chprecord',
            name='player_steal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='olympia.playerrecord'),
        ),
    ]
