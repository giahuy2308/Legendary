# Generated by Django 5.2.2 on 2025-06-14 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olympia', '0006_rename_player_answer_ttrecord_player_answers_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playerrecord',
            name='auth_id',
        ),
        migrations.AddField(
            model_name='playerrecord',
            name='no',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ttrecord',
            name='player_answers',
            field=models.JSONField(default=dict),
        ),
    ]
