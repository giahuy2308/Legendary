# Generated by Django 5.2.2 on 2025-06-18 15:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olympia', '0019_alter_chpquestion_options_alter_kdquestion_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chprecord',
            name='media',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='olympia.mediaresource'),
        ),
        migrations.AddField(
            model_name='kdrecord',
            name='media',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='olympia.mediaresource'),
        ),
        migrations.AddField(
            model_name='ttrecord',
            name='media',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='olympia.mediaresource'),
        ),
        migrations.AddField(
            model_name='vcnvrecord',
            name='media',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='olympia.mediaresource'),
        ),
        migrations.AddField(
            model_name='vdrecord',
            name='media',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='olympia.mediaresource'),
        ),
    ]
