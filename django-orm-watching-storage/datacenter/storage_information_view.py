from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render

from .utils import to_dict


def storage_information_view(request):
    # Программируем здесь

    visitors_in_storage = Visit.objects.filter(leaved_at=None)
    non_closed_visits = [to_dict(visitor) for visitor in visitors_in_storage]

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
