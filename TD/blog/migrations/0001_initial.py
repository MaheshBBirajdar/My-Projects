# Generated by Django 2.1 on 2023-04-19 06:32

import blog.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_id', models.IntegerField(unique=True)),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('reporting_person', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Artist1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_id1', models.IntegerField()),
                ('department', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('reporting', models.CharField(max_length=100)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IssuedShot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskassign', models.CharField(max_length=30)),
                ('projectname', models.CharField(max_length=30)),
                ('issuedate', models.DateField(auto_now=True)),
                ('expirydate', models.DateField(default=blog.models.get_expiry)),
            ],
        ),
        migrations.CreateModel(
            name='IssuedShot1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Shot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('task_assign', models.CharField(max_length=100)),
                ('work_description', models.CharField(max_length=200)),
                ('date_started', models.DateTimeField(default=django.utils.timezone.now)),
                ('work_status', models.CharField(max_length=100)),
                ('date_completed', models.DateField()),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Shot1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('shot_number', models.IntegerField()),
                ('task_assign', models.CharField(max_length=100)),
                ('work_description', models.CharField(max_length=200)),
                ('date_started', models.DateTimeField(default=django.utils.timezone.now)),
                ('work_status', models.CharField(max_length=100)),
                ('date_completed', models.DateField(blank=True, null=True)),
                ('supervisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='artist1',
            name='shot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Shot1'),
        ),
    ]