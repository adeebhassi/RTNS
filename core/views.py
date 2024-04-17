from django.shortcuts import render
from events.models import *
from datetime import date
from django.core.exceptions import ObjectDoesNotExist
from .models import *
# Create your views here.
from datetime import datetime, timedelta

def index(request):
    today = date.today()
    try:
        slider_images = SliderImage.objects.all()
        about_us = AboutUs.objects.first()
        patron = Patron.objects.all()
        gallery=Gallery.objects.all()
        upcoming_event = Event.objects.filter(date__gte=today).order_by('date').first()
        if upcoming_event:
            earliest_speech = Speech.objects.earliest('start_time')
            event_date = upcoming_event.date
            first_speech = Speech.objects.filter(event=upcoming_event).order_by('start_time').first()
            if first_speech:
                event_date_formatted = upcoming_event.date.strftime("%Y-%m-%d")
                event_time = first_speech.start_time.strftime("%H:%M:%S")
                event_datetime = datetime.combine(event_date, first_speech.start_time)
                current_datetime = datetime.now()
                remaining_days = (event_datetime - current_datetime).days
                contaxt = {
                    'event_date': event_date,
                    'event_time': event_time,
                    'event_date_formatted': event_date_formatted,
                    'remaining_days': remaining_days,
                    'gallery':gallery
                }
                return render(request, 'core/index.html', contaxt)
    except ObjectDoesNotExist:
        pass

    home_content = {
        'slider_images': slider_images,
        'about_us': about_us,
        'patron': patron,
    }
    return render(request, 'core/index.html', home_content)