from datacenter.models import Visit
from django.shortcuts import render
from datacenter.visit_duration import get_duration
from datacenter.visit_duration import format_duration
from datacenter.formtter_entered_at import format_entered_at


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at__isnull=True)
    for visit in visits:
        employee_name = str(visit.passcard.owner_name)
        entered_at = visit.entered_at
        duration = get_duration(visit)
        duration = format_duration(duration)
        entered_at = format_entered_at(entered_at)
        non_closed_visits = [
            {
                'who_entered': employee_name,
                'entered_at': entered_at,
                'duration': duration
            }
        ]
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
