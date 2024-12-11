from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):


    #шаг 10
    current_time =  localtime().replace(microsecond=0)
    visits = Visit.objects.filter(leaved_at__isnull=True)

    for visit in visits:
        print(f'{employee.passcard} - Зашёл в хранилище, время по Москве:')
        print(visit.entered_at)
        print()
        stay_time = current_time - visit.entered_at
        print("Находится в хранилище:")
        print(stay_time)

    #шаг 11
    employees_from_storage = Visit.objects.filter(leaved_at__isnull=True)
    for employee in employees_from_storage:
        employee_name = employee.passcard.owner_name
        print(employee_name)




    # Шаг 12
    current_time =  localtime().replace(microsecond=0)
    
    employees_from_storage = Visit.objects.filter(leaved_at__isnull=True)

    for employee in employees_from_storage:
        employee_name = employee.passcard.owner_name
        print(employee_name)




    non_closed_visits = [
        {
            'who_entered': 'Richard Shaw',
            'entered_at': '11-04-2018 25:34',
            'duration': '25:03',
        }
    ]
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
