import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402


def main():
    passcards = Passcard.objects.all()
    passcard = passcards[0]

    owner_name = passcard.owner_name
    passcode = passcard.passcode
    created_at = passcard.created_at
    is_active = passcard.is_active

    passcard_template = """
        owner_name: {}
        passcode: {}
        created_at: {}
        is_active: {}
    """
    passcard = passcard_template.format(owner_name, passcode,
                                        created_at, is_active)

    print(passcard)


if __name__ == '__main__':
    main()
