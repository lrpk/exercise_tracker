from django.contrib import admin
from .models import Records, DailyPushRecord, DailySitRecord, DailySquadRecord


class RecordsAdmin(admin.ModelAdmin):
    # list_filter = ("type", "total",)
    list_display = ("type", "total",)


# Register your models here.
admin.site.register(Records)
admin.site.register(DailyPushRecord)
admin.site.register(DailySitRecord)
admin.site.register(DailySquadRecord)
