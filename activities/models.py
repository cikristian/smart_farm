from django.db import models

from django.db import models


class Activity(models.Model):

    ACTIVITY_TYPES = [
        ('planting', 'Planting'),
        ('feeding', 'Feeding'),
        ('harvesting', 'Harvesting'),
        ('maintenance', 'Maintenance'),
        ('other', 'Other'),
    ]

    farm = models.ForeignKey(
        'farms.Farm',
        on_delete=models.CASCADE,
        related_name='activities'
    )
    activity_type = models.CharField(
        max_length=50,
        choices=ACTIVITY_TYPES
    )
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.activity_type} - {self.farm.name}"
