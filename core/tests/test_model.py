from django.test import TestCase
from django.utils import timezone
from core.models import Studio, Position, Worker, Game

class StudioModelTest(TestCase):
    def setUp(self):
        self.studio = Studio.objects.create(name="Epic Games", country="USA")

    def test_str_method(self):
        self.assertEqual(str(self.studio), "Epic Games")


class PositionModelTest(TestCase):
    def setUp(self):
        self.position = Position.objects.create(name="Developer")

    def test_str_method(self):
        self.assertEqual(str(self.position), "Developer")


class WorkerModelTest(TestCase):
    def setUp(self):
        self.studio = Studio.objects.create(name="Epic Games", country="USA")
        self.position = Position.objects.create(name="Developer")
        self.worker = Worker.objects.create_user(
            username="testuser",
            first_name="John",
            last_name="Doe",
            password="testpassword123",
            position=self.position,
            studio=self.studio
        )

    def test_str_method(self):
        self.assertEqual(str(self.worker), "Developer: John Doe")

    def test_get_absolute_url(self):
        url = self.worker.get_absolute_url()
        self.assertEqual(url, f"/workers/{self.worker.pk}/")


class GameModelTest(TestCase):
    def setUp(self):
        self.studio = Studio.objects.create(name="Epic Games", country="USA")
        self.position = Position.objects.create(name="Developer")
        self.worker = Worker.objects.create_user(
            username="testuser",
            first_name="John",
            last_name="Doe",
            password="testpassword123",
            position=self.position,
            studio=self.studio
        )
        self.game = Game.objects.create(
            name="Fortnite",
            genre="Battle Royale",
            description="A multiplayer game",
            release_date=timezone.now().date(),
            studio=self.studio
        )
        self.game.workers.add(self.worker)

    def test_str_method(self):
        expected = f"Fortnite Battle Royale A multiplayer game"
        self.assertEqual(str(self.game), expected)

    def test_workers_relation(self):
        self.assertIn(self.worker, self.game.workers.all())
