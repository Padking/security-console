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
    print(visits_per_passcard)


if __name__ == '__main__':
    main()
