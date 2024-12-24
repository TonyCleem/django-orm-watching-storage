from datacenter.models import Visit
from django.shortcuts import render
from datacenter.visit_time_formatter import format_duration, get_duration, format_entered_at


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at__isnull=True)
    for visit in visits:
        non_closed_visits = [
            {
                'who_entered': str(visit.passcard.owner_name),
                'entered_at': format_entered_at(visit.entered_at),
                'duration': format_duration(get_duration(visit))
            }
        ]
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
