from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
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


class StudioCreateView(generic.CreateView):
    model = Studio
    fields = "__all__"
    success_url = reverse_lazy('core:studio-list')


class StudioUpdateView(generic.UpdateView):
    model = Studio
    fields = "__all__"
    success_url = reverse_lazy('core:studio-list')


class StudioDeleteView(generic.DeleteView):
    model = Studio
    success_url = reverse_lazy('core:studio-list')

class WorkerListView(generic.ListView):
    model = Worker
    queryset = Worker.objects.all().prefetch_related('games__studio')
    paginate_by = 5


class WorkerDetailView(generic.DetailView):
    model = Worker


class WorkerCreateView(generic.CreateView):
    model = Worker
    fields = "__all__"
    success_url = reverse_lazy('core:worker-list')


class WorkerDeleteView(generic.DeleteView):
    model = Worker
    success_url = reverse_lazy('core:worker-list')


class GameListView(generic.ListView):
    model = Game
    queryset = Game.objects.all().select_related('studio')
    paginate_by = 5


class GameCreateView(generic.CreateView):
    model = Game
    fields = "__all__"
    success_url = reverse_lazy('core:game-list')


class GameUpdateView(generic.UpdateView):
    model = Game
    fields = "__all__"
    success_url = reverse_lazy('core:game-list')


class GameDeleteView(generic.DeleteView):
    model = Game
    success_url = reverse_lazy('core:game-list')
