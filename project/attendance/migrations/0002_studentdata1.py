# Generated by Django 4.0.6 on 2022-07-15 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Studentdata1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuid', models.IntegerField()),
                ('stuid_sub', models.CharField(max_length=100, unique=True)),
                ('stuname', models.CharField(max_length=100)),
                ('stumail', models.EmailField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
            ],
            options={
                'unique_together': {('stuid', 'subject')},
            },
        ),
    ]
