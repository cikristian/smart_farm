from django.db import models
from django.conf import settings


class Farm(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="farms"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name