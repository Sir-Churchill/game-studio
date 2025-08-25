from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Studio(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    class Meta:
        ordering =["name"]

    def __str__(self) -> str:
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name

class Worker(AbstractUser):
    position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name='workers')
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE, related_name='workers', null=True, blank=True)

    class Meta:
        verbose_name = 'worker'
        verbose_name_plural = 'workers'

    def __str__(self) -> str:
        return f"{self.position.name}: {self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("core:worker-detail", kwargs={"pk": self.pk})

class Game(models.Model):
    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE, related_name='games')
    workers = models.ManyToManyField(Worker, related_name='games')


    def __str__(self) -> str:
        return f"{self.name} {self.genre} {self.description}"