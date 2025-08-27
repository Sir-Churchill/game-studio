from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from core.forms import WorkerCreationForm, WorkerUpdateForm, GameForm, StudioSearchForm, WorkerSearchForm, \
    GameSearchForm
from core.models import Studio, Worker, Game

@login_required
def index(request: HttpRequest) -> HttpResponse:
    num_studios = Studio.objects.count()
    num_workers = Worker.objects.count()
    num_games = Game.objects.count()

    context = {
        'num_studio': num_studios,
        'num_worker': num_workers,
        'num_game': num_games,
    }

    return render(request,'core/index.html', context=context)


class StudioListView(LoginRequiredMixin ,generic.ListView):
    model = Studio
    queryset = Studio.objects.all()
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(StudioListView, self).get_context_data(**kwargs)
        context['search_form'] = StudioSearchForm(
            initial= {'name': self.request.GET.get('name', '')}
        )

        return context

    def get_queryset(self):

        form = StudioSearchForm(self.request.GET)
        if form.is_valid():
            return self.queryset.filter(name__icontains=form.cleaned_data['name'])
        return self.queryset


class StudioDetailView(LoginRequiredMixin ,generic.DetailView):
    model = Studio


class StudioCreateView(LoginRequiredMixin, generic.CreateView):
    model = Studio
    fields = "__all__"
    success_url = reverse_lazy('core:studio-list')


class StudioUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Studio
    fields = "__all__"
    success_url = reverse_lazy('core:studio-list')


class StudioDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Studio
    success_url = reverse_lazy('core:studio-list')

class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    queryset = Worker.objects.all().prefetch_related('games__studio')
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(WorkerListView, self).get_context_data(**kwargs)
        context['search_form'] = WorkerSearchForm(
            initial= {'name': self.request.GET.get('username', '')}
        )
        return context

    def get_queryset(self):
        form = WorkerSearchForm(self.request.GET)
        if form.is_valid():
            return self.queryset.filter(username__icontains=form.cleaned_data['username'])
        return self.queryset


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker


class WorkerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Worker
    form_class = WorkerCreationForm
    success_url = reverse_lazy('core:worker-list')


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    form_class = WorkerUpdateForm
    success_url = reverse_lazy('core:worker-list')

class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Worker
    success_url = reverse_lazy('core:worker-list')


class GameListView(LoginRequiredMixin, generic.ListView):
    model = Game
    queryset = Game.objects.all().select_related('studio')
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GameListView, self).get_context_data(**kwargs)
        context['search_form'] = GameSearchForm(
            initial= {'name': self.request.GET.get('name', '')}
        )
        return context

    def get_queryset(self):
        form = GameSearchForm(self.request.GET)
        if form.is_valid():
            return self.queryset.filter(name__icontains=form.cleaned_data['name'])
        return self.queryset

class GameCreateView(LoginRequiredMixin, generic.CreateView):
    model = Game
    form_class = GameForm
    success_url = reverse_lazy('core:game-list')


class GameUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Game
    form_class = GameForm
    success_url = reverse_lazy('core:game-list')


class GameDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Game
    success_url = reverse_lazy('core:game-list')

def toggle_assign_to_studio(request, pk):
    worker = request.user
    studio = Studio.objects.get(id=pk)

    if worker.studio == studio:
        worker.studio = None
    else:
        worker.studio = studio

    worker.save()
    return HttpResponseRedirect(reverse_lazy('core:studio-detail', args=[pk]))