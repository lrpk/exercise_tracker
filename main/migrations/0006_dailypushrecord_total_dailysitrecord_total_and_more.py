# Generated by Django 5.0.1 on 2024-02-19 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_dailypushrecord_dailysitrecord_dailysquadrecord_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailypushrecord',
            name='total',
            field=models.CharField(default=0, max_length=10000),
        ),
        migrations.AddField(
            model_name='dailysitrecord',
            name='total',
            field=models.CharField(default=0, max_length=10000),
        ),
        migrations.AddField(
            model_name='dailysquadrecord',
            name='total',
            field=models.CharField(default=0, max_length=10000),
        ),
    ]
