from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from core.models import Studio, Worker, Game


def index(request: HttpRequest) -> HttpResponse:
    num_studios = Studio.objects.count()
    num_worker = Worker.objects.count()
    num_game = Game.objects.count()

    context = {
        'num_studios': num_studios,
        'num_worker': num_worker,
        'num_game': num_game,
    }

    return render(request,'core/index.html', context=context)