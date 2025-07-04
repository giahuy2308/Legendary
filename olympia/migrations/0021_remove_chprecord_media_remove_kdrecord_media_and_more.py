# Generated by Django 5.2.2 on 2025-06-18 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olympia', '0020_chprecord_media_kdrecord_media_ttrecord_media_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chprecord',
            name='media',
        ),
        migrations.RemoveField(
            model_name='kdrecord',
            name='media',
        ),
        migrations.RemoveField(
            model_name='ttrecord',
            name='media',
        ),
        migrations.RemoveField(
            model_name='vcnvrecord',
            name='media',
        ),
        migrations.RemoveField(
            model_name='vdrecord',
            name='media',
        ),
        migrations.AddField(
            model_name='chprecord',
            name='media',
            field=models.ManyToManyField(to='olympia.mediaresource'),
        ),
        migrations.AddField(
            model_name='kdrecord',
            name='media',
            field=models.ManyToManyField(to='olympia.mediaresource'),
        ),
        migrations.AddField(
            model_name='ttrecord',
            name='media',
            field=models.ManyToManyField(to='olympia.mediaresource'),
        ),
        migrations.AddField(
            model_name='vcnvrecord',
            name='media',
            field=models.ManyToManyField(to='olympia.mediaresource'),
        ),
        migrations.AddField(
            model_name='vdrecord',
            name='media',
            field=models.ManyToManyField(to='olympia.mediaresource'),
        ),
    ]
