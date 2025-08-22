from django.urls import path

from .views import (index,
                    StudioListView,
                    GameListView,
                    WorkerListView,
                    StudioDetailView,
                    WorkerDetailView
                    )

urlpatterns = [
    path('', index, name='index'),
    path('studios/', StudioListView.as_view(), name='studio-list'),
    path('studios/<int:pk>/', StudioDetailView.as_view(), name='studio-detail'),
    path('workers/', WorkerListView.as_view(), name='worker-list'),
    path('workers/<int:pk>/', WorkerDetailView.as_view(), name='worker-detail'),
    path('games/', GameListView.as_view(), name='game-list'),

]

app_name = 'core'