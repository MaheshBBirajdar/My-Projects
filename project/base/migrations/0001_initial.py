# Generated by Django 4.0.6 on 2022-07-13 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuid', models.IntegerField()),
                ('stuname', models.CharField(max_length=100)),
                ('stumail', models.EmailField(max_length=100)),
                ('stuclass', models.CharField(max_length=100)),
            ],
        ),
    ]
