from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from visit_timer import format_duration
from datacenter.models import is_visit_long


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(owner_name="Breanna Campbell")
    visits = Visit.objects.filter(passcard=passcard, leaved_at__isnull=False)



    for visit in visits:
        duration_visit_time = get_duration(visit)
        duration_visit_time = int(duration_visit_time.total_seconds())
        duration_visit_time = format_duration(duration_visit_time)


        visit_time_in_min = int(duration_visit_time // 60)

        this_passcard_visits = [
            {
                'entered_at': visit.entered_at,
                'duration': duration_visit_time,
                'is_strange': False
            },
        ]

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
