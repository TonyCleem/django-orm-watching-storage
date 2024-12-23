from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from datacenter.visit_duration import format_duration, get_duration
from datacenter.models import is_visit_long
from datacenter.formtter_entered_at import format_entered_at


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    for visit in visits:
        entered_at = visit.entered_at
        duration_visit_time = get_duration(visit)
        entered_at = format_entered_at(entered_at)
        this_passcard_visits = [
            {
                'entered_at': entered_at,
                'duration': format_duration(duration_visit_time),
                'is_strange': is_visit_long(duration_visit_time)
            },
        ]
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
