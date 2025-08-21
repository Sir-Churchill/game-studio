from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from core.models import Studio, Worker, Game


def index(request: HttpRequest) -> HttpResponse:
    num_studios = Studio.objects.count()
    num_workers = Worker.objects.count()
    num_games = Game.objects.count()

    context = {
        'num_studios': num_studios,
        'num_worker': num_workers,
        'num_game': num_games,
    }

    return render(request,'core/index.html', context=context)