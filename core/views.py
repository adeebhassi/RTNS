from django.shortcuts import render
from events.models import *
from datetime import date
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def index(requst):
    today=date.today()
    try:
        upcoming_event=Event.objects.filter(date__gte=today).order_by('date').first()
        if upcoming_event:
            earliest_speech=Speech.objects.earliest('start_time')
            event_date=upcoming_event.date
            first_speech = Speech.objects.filter(event=upcoming_event).order_by('start_time').first()
            if first_speech:
                event_date_formatted=upcoming_event.date.strftime("%Y-%m-%d")
                event_time=first_speech.start_time.strftime( "%H:%M:%S" ) 
                contaxt={
                    'event_date':event_date,
                    'event_time':event_time,
                    'event_date_formatted':event_date_formatted
                }
                return render(requst,'core/index.html',contaxt)
    except ObjectDoesNotExist:
        pass
    return render(requst,'core/index.html',{})
