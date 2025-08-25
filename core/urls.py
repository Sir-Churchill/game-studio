from django.urls import path

from .views import (index,
                    StudioListView,
                    StudioDetailView,
                    StudioCreateView,
                    StudioUpdateView,
                    StudioDeleteView,
                    GameListView,
                    GameCreateView,
                    GameUpdateView,
                    GameDeleteView,
                    WorkerListView,
                    WorkerDetailView,
                    WorkerCreateView,
                    WorkerDeleteView, WorkerUpdateView, toggle_assign_to_studio

                    )

urlpatterns = [
    path('', index, name='index'),
    path('studios/<int:pk>/toggle-assign/', toggle_assign_to_studio, name='toggle_assign_to_studio'),
    path('studios/', StudioListView.as_view(), name='studio-list'),
    path('studios/create/', StudioCreateView.as_view(), name='studio-create'),
    path('studios/<int:pk>/update/', StudioUpdateView.as_view(), name='studio-update'),
    path('studios/<int:pk>/delete/', StudioDeleteView.as_view(), name='studio-delete'),
    path('studios/<int:pk>/', StudioDetailView.as_view(), name='studio-detail'),
    path('workers/', WorkerListView.as_view(), name='worker-list'),
    path('workers/<int:pk>/', WorkerDetailView.as_view(), name='worker-detail'),
    path('workers/create/', WorkerCreateView.as_view(), name='worker-create'),
    path('workers/<int:pk>/update/', WorkerUpdateView.as_view(), name='worker-update'),
    path('workers/<int:pk>/delete/', WorkerDeleteView.as_view(), name='worker-delete'),
    path('games/', GameListView.as_view(), name='game-list'),
    path('games/create/', GameCreateView.as_view(), name='game-create'),
    path('games/<int:pk>/update/', GameUpdateView.as_view(), name='game-update'),
    path('games/<int:pk>/delete/', GameDeleteView.as_view(), name='game-delete'),

]

app_name = 'core'