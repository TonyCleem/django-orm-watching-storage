import locale
from datetime import datetime


locale.setlocale(locale.LC_ALL, "")


def format_entered_at(entered_at):
    entered_at = f"{entered_at.day} {entered_at.strftime('%B')} {entered_at.year} г. {entered_at.strftime('%H:%M')}"
    return entered_at