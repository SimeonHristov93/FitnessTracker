from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from .validators import validate_name_length, validate_description_length


class Workout(models.Model):
    WORKOUT_TYPES = [
        ('strength', 'Strength Training'),
        ('cardio', 'Cardio'),
        ('hiit', 'HIIT'),
        ('flexibility', 'Flexibility'),
        ('endurance', 'Endurance'),
    ]

    name = models.CharField(max_length=100, validators=[validate_name_length])
    description = models.TextField(validators=[validate_description_length])
    workout_type = models.CharField(
        max_length=20,
        choices=WORKOUT_TYPES
    )
    duration_minutes = models.IntegerField(
        validators=[MinValueValidator(5), MaxValueValidator(300)],
    )
    difficulty = models.IntegerField(
        choices=[(1, 'Beginner'), (2, 'Intermediate'), (3, 'Advanced')],
        default=1,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.get_workout_type_display()})"

    class Meta:
        ordering = ['-created_at']
