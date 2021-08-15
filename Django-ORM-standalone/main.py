import datetime
import os

import django
from django.utils.timezone import localtime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402
from datacenter.models import Visit


def main():
    visitors_in_vault = Visit.objects.filter(leaved_at=None)
    for visitor in visitors_in_vault:
        print(visitor.passcard.owner_name)


if __name__ == '__main__':
    main()
