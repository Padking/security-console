import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402


def main():
    passcards = Passcard.objects.all()

    active_passcards = []
    for passcard in passcards:
        if passcard.is_active:
            active_passcards.append(passcard)

    passcards_count_template = "Всего пропусков {}"
    passcards_count = passcards_count_template.format(len(passcards))

    active_passcards_template = "Активных пропусков {}"
    active_passcards = active_passcards_template.format(len(active_passcards))

    print(passcards_count, active_passcards, sep="\n")


if __name__ == '__main__':
    main()
