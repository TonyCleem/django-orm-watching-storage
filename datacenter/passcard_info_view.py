from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from datacenter.visit_time_formatter import format_duration, get_duration, is_visit_long, format_entered_at


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    for visit in visits:
        this_passcard_visits = [
            {
                'entered_at': format_entered_at(visit.entered_at),
                'duration': format_duration(get_duration(visit)),
                'is_strange': is_visit_long(get_duration(visit))
            },
        ]
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
