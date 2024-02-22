from django.db import models

from time import strftime, gmtime


# Create your models here.
class Records(models.Model):
    type = models.CharField(max_length=20, default=0)
    total = models.CharField(max_length=10000)

    def __str__(self):
        return self.type


class DailyPushRecord(models.Model):
    total = models.CharField(max_length=10000, default=0)
    today_total = models.CharField(max_length=1000, default=0)
    reps = models.CharField(max_length=1000, default=0)
    current_time = models.CharField(max_length=50)


class DailySitRecord(models.Model):
    total = models.CharField(max_length=10000, default=0)
    today_total = models.CharField(max_length=1000, default=0)
    reps = models.CharField(max_length=1000, default=0)
    current_time = models.CharField(max_length=50)


class DailySquadRecord(models.Model):
    total = models.CharField(max_length=10000, default=0)
    today_total = models.CharField(max_length=1000, default=0)
    reps = models.CharField(max_length=1000, default=0)
    current_time = models.CharField(max_length=50)
