from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from core.models import Studio, Position, Worker, Game

class CoreViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.studio = Studio.objects.create(name="Epic Games", country="USA")
        self.position = Position.objects.create(name="Developer")
        self.user = Worker.objects.create_user(
            username="admin",
            password="testpass123",
            first_name="Admin",
            last_name="User",
            studio=self.studio,
            position=self.position,
            is_staff=True,
            is_superuser=True
        )
        self.client.login(username="admin", password="testpass123")
        self.game = Game.objects.create(
            name="Fortnite",
            genre="Battle Royale",
            description="Multiplayer game",
            release_date=timezone.now().date(),
            studio=self.studio
        )
        self.game.workers.add(self.user)

    def test_index_view(self):
        response = self.client.get(reverse("core:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "core/index.html")

    def test_studio_list_view(self):
        response = self.client.get(reverse("core:studio-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.studio.name)
        self.assertTemplateUsed(response, "core/studio_list.html")

    def test_studio_detail_view(self):
        response = self.client.get(reverse("core:studio-detail", kwargs={"pk": self.studio.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.studio.name)

    def test_worker_list_view(self):
        response = self.client.get(reverse("core:worker-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user.username)