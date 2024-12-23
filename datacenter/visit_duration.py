from django.utils.timezone import localtime


SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60


def get_duration(visit):
    if visit.leaved_at:
        duration = visit.leaved_at - visit.entered_at
        return duration
    current_time =  localtime().replace(microsecond=0)
    duration = current_time - visit.entered_at
    return duration


def format_duration(duration):
    hours = int(duration.total_seconds() // SECONDS_IN_HOUR)
    minutes = int((duration.total_seconds() % SECONDS_IN_HOUR) // SECONDS_IN_MINUTE)
    duration =  f'{hours}ч {minutes}мин'
    return duration