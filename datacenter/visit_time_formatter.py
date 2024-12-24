import locale
from datetime import datetime
from django.utils.timezone import localtime


locale.setlocale(locale.LC_ALL, "")


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


def is_visit_long(duration_visit, minutes=60):
    duration_visit = int(duration_visit.total_seconds() // SECONDS_IN_MINUTE)
    return duration_visit > minutes


def format_entered_at(entered_at):
    entered_at = f"{entered_at.day} {entered_at.strftime('%B')} {entered_at.year} г. {entered_at.strftime('%H:%M')}"
    return entered_at


