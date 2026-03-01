from django.db import models

class PredictionRecord(models.Model):

    RECOMMENDATIONS = [
        ('buy', 'Buy'),
        ('sell', 'Sell'),
        ('hold', 'Hold'),
    ]

    farm = models.ForeignKey(
        'farms.Farm',
        on_delete=models.CASCADE,
        related_name='predictions'
    )

    recommendation = models.CharField(
        max_length=10,
        choices=RECOMMENDATIONS
    )

    confidence_score = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.recommendation} ({self.confidence_score})"
