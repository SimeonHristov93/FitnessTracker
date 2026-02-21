from django.db import models
from django.db import models
from django.core.validators import MinValueValidator
from workouts.models import Workout
from .validators import validate_rest_time, validate_name_length, validate_max_reps, validate_max_sets


class Exercise(models.Model):
    EQUIPMENT_CHOICES = [
        ('none', 'No Equipment'),
        ('dumbbells', 'Dumbbells'),
        ('barbell', 'Barbell'),
        ('machine', 'Machine'),
        ('bands', 'Resistance Bands'),
        ('bodyweight', 'Bodyweight'),
    ]

    MUSCLE_GROUPS = [
        ('chest', 'Chest'),
        ('back', 'Back'),
        ('legs', 'Legs'),
        ('shoulders', 'Shoulders'),
        ('arms', 'Arms'),
        ('core', 'Core'),
        ('full', 'Full Body'),
        ('cardio', 'Cardio'),
    ]

    name = models.CharField(max_length=100, validators=[validate_name_length])
    description = models.TextField()
    muscle_group = models.CharField(
        max_length=20,
        choices=MUSCLE_GROUPS
    )
    equipment = models.CharField(
        max_length=20,
        choices=EQUIPMENT_CHOICES
    )
    sets = models.IntegerField(
        validators=[MinValueValidator(1), validate_max_sets],
        default=3
    )
    reps = models.IntegerField(
        validators=[MinValueValidator(1), validate_max_reps],
        default=10,
    )
    rest_seconds = models.IntegerField(
        default=60,
        help_text="Resting time between sets in seconds",
        validators=[validate_rest_time]
    )
    workout = models.ForeignKey(
        Workout,
        on_delete=models.CASCADE,
        related_name='exercises'
    )

    def __str__(self):
        return f"{self.name} ({self.get_muscle_group_display()})"
