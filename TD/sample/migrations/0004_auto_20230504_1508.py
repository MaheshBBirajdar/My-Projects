# Generated by Django 3.2.18 on 2023-05-04 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0003_auto_20230504_1223'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='id',
            new_name='lid',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='id',
            new_name='pid',
        ),
    ]
