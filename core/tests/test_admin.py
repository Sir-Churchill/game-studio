from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse
from core.models import Studio, Position, Worker

class AdminIntegrationTest(TestCase):
    def setUp(self):
        # Создаем Studio и Position для workers
        self.studio = Studio.objects.create(name="Test Studio", country="Test Country")
        self.position = Position.objects.create(name="Test Position")

        # Клиент
        self.client = Client()

        # Суперпользователь с обязательными полями
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="test1234",
            studio=self.studio,     # обязательное поле
            position=self.position, # обязательное поле
        )
        self.client.force_login(self.admin_user)

        # Обычный worker
        self.worker = get_user_model().objects.create_user(
            username="worker1",
            password="worker123",
            studio=self.studio,
            position=self.position,
        )

    def test_worker_listed_in_admin(self):
        url = reverse("admin:core_worker_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.worker.username)

    def test_studio_listed_in_admin(self):
        url = reverse("admin:core_studio_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.studio.name)
