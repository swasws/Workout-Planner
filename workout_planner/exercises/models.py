from django.db import models
from django.contrib.auth.models import User

class Exercise(models.Model):
    CATEGORY_CHOICES = [
        ('cardio', 'Cardio'),
        ('strength', 'Strength'),
        ('flexibility', 'Flexibility'),
        ('balance', 'Balance'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    sets = models.IntegerField(default=1)
    repetitions = models.IntegerField(default=10)
    duration_in_minutes = models.FloatField(blank=True, null=True)
    weight_in_kg = models.FloatField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


