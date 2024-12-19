from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from visit_timer import get_duration
from visit_timer import format_duration


def storage_information_view(request):

    # Шаг 12
    visits = Visit.objects.filter(leaved_at__isnull=True)
    for visit in visits:
        employee_name = str(visit.passcard.owner_name)
        entered_at = visit.entered_at
        duration = get_duration(visit)
        duration = format_duration(duration)

        months = {
                1: "января", 2: "февраля", 3: "марта", 4: "апреля", 5: "мая", 6: "июня",
                7: "июля", 8: "августа", 9: "сентября", 10: "октября", 11: "ноября", 12: "декабря"
            }

        entered_at = f"{entered_at.day} {months[entered_at.month]} {entered_at.year} г. {entered_at.strftime('%H:%M')}"
        
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
