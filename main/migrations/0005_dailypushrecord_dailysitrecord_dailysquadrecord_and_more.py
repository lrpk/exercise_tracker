# Generated by Django 5.0.1 on 2024-02-19 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_dailyrecord_records_delete_push_delete_sit_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyPushRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('today_total', models.CharField(default=0, max_length=1000)),
                ('reps', models.CharField(default=0, max_length=1000)),
                ('current_time', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DailySitRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('today_total', models.CharField(default=0, max_length=1000)),
                ('reps', models.CharField(default=0, max_length=1000)),
                ('current_time', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DailySquadRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('today_total', models.CharField(default=0, max_length=1000)),
                ('reps', models.CharField(default=0, max_length=1000)),
                ('current_time', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='DailyRecord',
        ),
    ]