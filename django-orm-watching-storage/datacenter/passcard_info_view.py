from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

from datacenter.models import Passcard
from datacenter.models import Visit

from .utils import visit_to_dict


def passcard_info_view(request, passcode):
    # Программируем здесь

    try:
        passcard = Passcard.objects.get(passcode=passcode)
    except ObjectDoesNotExist:
        print(f'Passcard with {passcode} doesn\'t exist')
    else:
        visits_per_passcard = passcard.visit_set.all()  # возможно ли оформить в одной строке?
        this_passcard_visits = [visit_to_dict(visit) for visit in visits_per_passcard]

        context = {
            'passcard': passcard,
            'this_passcard_visits': this_passcard_visits
        }
        return render(request, 'passcard_info.html', context)
