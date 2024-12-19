from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from timer import format_duration, get_duration
from datacenter.models import is_visit_long


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard, leaved_at__isnull=False)

    for visit in visits:
        entered_at = visit.entered_at
        duration_visit_time = get_duration(visit)
        duration_visit_time = format_duration(duration_visit_time)
        months = {
            1: "января", 2: "февраля", 3: "марта", 4: "апреля", 5: "мая", 6: "июня",
            7: "июля", 8: "августа", 9: "сентября", 10: "октября", 11: "ноября", 12: "декабря"
        }
        entered_at = f"{entered_at.day} {months[entered_at.month]} {entered_at.year} г. {entered_at.strftime('%H:%M')}"

        this_passcard_visits = [
            {
                'entered_at': entered_at,
                'duration': duration_visit_time,
                'is_strange': False
            },
        ]
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
