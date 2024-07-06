# countdown/views.py

from django.shortcuts import render
import datetime

def newyeareve(request):
    today = datetime.date.today()
    is_new_years_eve = (today.month == 12 and today.day == 31)

    context = {
        'is_new_years_eve': is_new_years_eve,
        'today': today,
    }
    return render(request, 'countdown/newyeareve.html', context)
