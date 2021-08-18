from django.shortcuts import get_object_or_404, \
                             render

from datacenter.models import Passcard
from datacenter.models import Visit

from .utils import to_dict


def passcard_info_view(request, passcode):

    passcard = get_object_or_404(Passcard, passcode=passcode)

    visits_per_passcard = passcard.visit_set.all()
    this_passcard_visits = [to_dict(visit) for visit in visits_per_passcard]

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
