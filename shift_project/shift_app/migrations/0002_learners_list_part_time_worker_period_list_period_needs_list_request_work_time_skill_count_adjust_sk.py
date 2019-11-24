# Generated by Django 2.2.7 on 2019-11-24 05:41

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('shift_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Part_time_worker',
            fields=[
                ('worker_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('worker_name', models.CharField(max_length=128)),
                ('work_times', models.IntegerField()),
                ('request_times', models.IntegerField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Period_list',
            fields=[
                ('period_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('period_name', models.CharField(max_length=128)),
                ('start_date', models.DateTimeField(default=datetime.datetime.now)),
                ('finish_date', models.DateTimeField(default=datetime.datetime.now)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill_list',
            fields=[
                ('skill_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('skill_name', models.CharField(max_length=128)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Store_registration',
            fields=[
                ('store_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('store_name', models.CharField(max_length=128)),
                ('opening_time', models.DateTimeField(default=datetime.datetime.now)),
                ('closing_time', models.DateTimeField(default=datetime.datetime.now)),
                ('place', models.CharField(max_length=128)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Time_list',
            fields=[
                ('time_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('time_name', models.CharField(max_length=128)),
                ('opening_time', models.DateTimeField(default=datetime.datetime.now)),
                ('closing_time', models.DateTimeField(default=datetime.datetime.now)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='skill_count_adjust',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ajust_count', models.IntegerField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
                ('skill_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shift_app.Skill_list')),
                ('time_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shift_app.Time_list')),
            ],
        ),
        migrations.CreateModel(
            name='request_work_time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('start_time', models.DateTimeField(default=datetime.datetime.now)),
                ('finish_time', models.DateTimeField(default=datetime.datetime.now)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
                ('worker_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shift_app.Part_time_worker')),
            ],
        ),
        migrations.CreateModel(
            name='Period_needs_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_people', models.IntegerField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
                ('period_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shift_app.Period_list')),
                ('skill_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shift_app.Skill_list')),
            ],
        ),
        migrations.CreateModel(
            name='learners_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
                ('skill_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shift_app.Skill_list')),
                ('worker_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shift_app.Part_time_worker')),
            ],
        ),
    ]
