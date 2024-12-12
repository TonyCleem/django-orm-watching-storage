from django.utils.timezone import localtime


def get_duration(visit):

    current_time =  localtime().replace(microsecond=0)
    duration = current_time - visit.entered_at
    return duration


def format_duration(duration):
    seconds = int(duration.total_seconds())
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)

    duration =  f'{hours}ч {minutes}мин'
    
    return duration