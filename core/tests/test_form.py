from django.test import TestCase
from django.contrib.auth import get_user_model
from core.models import Studio, Position, Worker, Game
from core.forms import GameForm, WorkerCreationForm
from django.utils import timezone

User = get_user_model()

class GameFormTest(TestCase):
    def setUp(self):
        self.studio = Studio.objects.create(name="Epic Games", country="USA")
        self.position = Position.objects.create(name="Developer")
        self.worker = Worker.objects.create_user(
            username="john",
            password="testpass123",
            first_name="John",
            last_name="Doe",
            studio=self.studio,
            position=self.position
        )

    def test_game_form_valid_data(self):
        form_data = {
            "name": "Fortnite",
            "genre": "Battle Royale",
            "description": "Multiplayer game",
            "release_date": timezone.now().date(),
            "studio": self.studio.pk,
            "workers": [self.worker.pk]
        }
        form = GameForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_game_form_no_data(self):
        form = GameForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)
        self.assertIn("genre", form.errors)
        self.assertIn("description", form.errors)
        self.assertIn("release_date", form.errors)
        self.assertIn("studio", form.errors)


class WorkerCreationFormTest(TestCase):
    def setUp(self):
        self.studio = Studio.objects.create(name="Epic Games", country="USA")
        self.position = Position.objects.create(name="Developer")

    def test_worker_creation_form_valid_data(self):
        form_data = {
            "username": "johndoe",
            "password1": "complexpass123",
            "password2": "complexpass123",
            "first_name": "John",
            "last_name": "Doe",
            "studio": self.studio.pk,
            "position": self.position.pk
        }
        form = WorkerCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_worker_creation_form_invalid_password(self):
        form_data = {
            "username": "johndoe",
            "password1": "123",
            "password2": "123",
            "first_name": "John",
            "last_name": "Doe",
            "studio": self.studio.pk,
            "position": self.position.pk
        }
        form = WorkerCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("password2", form.errors)