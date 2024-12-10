import os

import django



from django.core.management import execute_from_command_line
from datacenter.models import Visit

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
execute_from_command_line('manage.py runserver 0.0.0.0:8000'.split())
django.setup()

if __name__ == '__main__':

    
    not_leaved_visits = Visit.objects.filter(leaved_at__isnull=True)
    print(not_leaved_visits)
