import datetime
import os

import django
from django.utils.timezone import localtime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard, \
                              Visit  # noqa: E402


def main():
    passcard = Passcard.objects.all()[0]
    visits_per_passcard = passcard.visit_set.all()

    min_threshold, max_threshold = 10, 1000
    visits_above_min_threshold, visits_above_max_threshold = [], []
    for visit in visits_per_passcard:
        if visit.is_visit_long(minutes=min_threshold):
            visits_above_min_threshold.append(visit)
        elif visit.is_visit_long(minutes=max_threshold):
            visits_above_max_threshold.append(visit)

    about_visits_template = "Визиты дольше {} мин {}"
    about_visits = zip((min_threshold, max_threshold), (visits_above_min_threshold, visits_above_max_threshold))
    for minutes, visits in about_visits:
        suspicious_visits = about_visits_template.format(minutes, visits)
        print(suspicious_visits)


if __name__ == '__main__':
    main()
