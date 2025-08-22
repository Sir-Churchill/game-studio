from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic

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

class StudioListView(generic.ListView):
    model = Studio
    paginate_by = 5


class StudioDetailView(generic.DetailView):
    model = Studio


class WorkerListView(generic.ListView):
    model = Worker
    queryset = Worker.objects.all().prefetch_related('games__studio')
    paginate_by = 5


class WorkerDetailView(generic.DetailView):
    model = Worker


class GameListView(generic.ListView):
    model = Game
    queryset = Game.objects.all().select_related('studio')
    paginate_by = 5
