from datetime import datetime, timedelta

from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import DailyPushRecord, DailySitRecord, DailySquadRecord
from .forms import ExerciseForm

import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl


# Create your views here.
def index(request):
    push_ups_today = DailyPushRecord.objects.last()
    sit_ups_today = DailySitRecord.objects.last()
    squads_today = DailySquadRecord.objects.last()

    date = datetime.now().strftime("%a, %d %b %Y")

    def get_data(exercise_type, get_form, exercise_obj):
        if request.method == "POST":
            exercise_reps = get_form.cleaned_data[exercise_type]
            if exercise_obj is not None:
                if date == exercise_obj.current_time:
                    exercise_total = int(exercise_obj.total) + int(exercise_reps)
                    exercise_today_total = int(exercise_obj.today_total) + int(exercise_reps)
                else:
                    exercise_total = int(exercise_obj.total) + int(exercise_reps)
                    exercise_today_total = exercise_reps
            else:
                exercise_total = exercise_reps
                exercise_today_total = exercise_reps

            return {
                'total': exercise_total,
                'today_total': exercise_today_total,
                'reps': exercise_reps,
                'current_time': date
            }

    def post(data, model_name):
        try:
            exercise_name = data
            new_exercise_record = model_name(total=exercise_name['total'],
                                             today_total=exercise_name['today_total'],
                                             reps=exercise_name['reps'],
                                             current_time=exercise_name['current_time'])
            new_exercise_record.save()

        except Exception as e:
            print(e)
            return HttpResponseRedirect('/main')

    print("Index")

    # form handling
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            post(get_data("push_ups", form, push_ups_today), DailyPushRecord)
            post(get_data("sit_ups", form, sit_ups_today), DailySitRecord)
            post(get_data("squads", form, squads_today), DailySquadRecord)
    else:
        form = ExerciseForm()

    # load last record
    push_ups_today = DailyPushRecord.objects.last()
    sit_ups_today = DailySitRecord.objects.last()
    squads_today = DailySquadRecord.objects.last()

    return render(request, "main/index.html", {
        "push_ups_today": push_ups_today,
        "sit_ups_today": sit_ups_today,
        "squads_today": squads_today,
        "form": form,
        "current_date": date,
    })


def stats(request):

    push_ups_obj = DailyPushRecord.objects.all()
    sit_ups_obj = DailySitRecord.objects.all()
    squads_obj = DailySquadRecord.objects.all()

    daily_push_records = []
    daily_sit_records = []
    daily_squad_records = []

    plots_push_records = []

    current_date = datetime.now()
    # Get the last three days
    last_three_days = [(current_date - timedelta(days=i)).strftime("%a, %d %b %Y") for i in range(3)]
    last_ten_days = [(current_date - timedelta(days=i)).strftime("%a, %d %b %Y") for i in range(10)]

    # Format and print the last three days
    def last_data(filter_lst, exercise_obj, num_of_days):
        for day in num_of_days:
            last_record = exercise_obj.filter(current_time=day).last()

            if last_record is not None:
                filter_lst.append(last_record)
            else:
                continue

# ==================================================================================

#  Фільтрую інформацію за останні десять днів та роблю з неї графік який має передатися
#  на сторінку "stats.html"

    # plot
    days = []
    reps = []

    last_data(plots_push_records, push_ups_obj, last_ten_days)
    fig, ax = plt.subplots()
    push_ups_plot = ax.plot(days, reps)

# ===================================================================================

    last_data(daily_push_records, push_ups_obj, last_three_days)
    last_data(daily_sit_records, sit_ups_obj, last_three_days)
    last_data(daily_squad_records, squads_obj, last_three_days)

    return render(request, "main/stats.html", {
        "daily_push_records": daily_push_records,
        "daily_sit_records": daily_sit_records,
        "daily_squad_records": daily_squad_records,
        "push_ups_plot": push_ups_plot,
    })
