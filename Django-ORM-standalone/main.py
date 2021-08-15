import datetime
import os

import django
from django.utils.timezone import localtime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402
from datacenter.models import Visit


def transform_repr(time: datetime.timedelta) -> str:
    seconds_to_transform = time.total_seconds()
    hours, time_remainder = divmod(seconds_to_transform, 60 * 60)
    minutes, seconds = divmod(time_remainder, 60)

    time_template = "{:.0f}:{:.0f}:{:.0f}"
    time_repr = time_template.format(hours, minutes, seconds)

    return time_repr


def main():
    passcards_count = Passcard.objects.count()
    active_passcards = Passcard.objects.filter(is_active=True)

    passcards_count_template = "Всего пропусков {}"
    passcards_count_msg = passcards_count_template.format(passcards_count)

    active_passcards_template = "Активных пропусков {}"
    active_passcards_msg = active_passcards_template.format(len(active_passcards))

    visits = Visit.objects.all()
    in_vault = Visit.objects.filter(leaved_at=None)

    visitors = Visit.objects.exclude(leaved_at=None)
    for visitor in visitors:
        entry_time = visitor.entered_at
        entry_localtime = localtime(entry_time)

        leaved_at_time = visitor.leaved_at
        leaved_at_localtime = localtime(leaved_at_time)

        timedelta = leaved_at_localtime - entry_localtime
        time_in_bank_vault = transform_repr(timedelta)

        entry_time_template = """
            Зашёл в хранилище, время по Москве:
            {}\n
            Находится в хранилище:
            {}
        """
        time_in_vault_msg = entry_time_template.format(entry_localtime,
                                                       time_in_bank_vault)
        print(time_in_vault_msg)


if __name__ == '__main__':
    main()
