import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402
from datacenter.models import Visit


def main():
    passcards_count = Passcard.objects.count()
    active_passcards = Passcard.objects.filter(is_active=True)

    passcards_count_template = "Всего пропусков {}"
    passcards_count_msg = passcards_count_template.format(passcards_count)

    active_passcards_template = "Активных пропусков {}"
    active_passcards_msg = active_passcards_template.format(len(active_passcards))

    visits = Visit.objects.all()

    print(passcards_count_msg, active_passcards_msg, visits, sep="\n")


if __name__ == '__main__':
    main()
