# Generated by Django 3.2.5 on 2021-09-19 00:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_auto_20210919_0606'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reading',
            old_name='device_id',
            new_name='reading_id',
        ),
    ]
