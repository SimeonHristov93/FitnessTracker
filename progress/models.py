from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from workouts.models import Workout
from .validators import validate_no_future_date, validate_max_calories, validate_max_duration


class WorkoutLog(models.Model):
    workout = models.ForeignKey(
        Workout,
        on_delete=models.CASCADE,
        related_name='logs',
    )
    completed_at = models.DateTimeField(
        default=timezone.now,
        validators=[validate_no_future_date]
    )
    duration_minutes = models.PositiveIntegerField(
        validators=[MinValueValidator(1), validate_max_duration],
        help_text="Duration in minutes"
    )
    calories_burned = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="Optional: Estimated calories burned",
        validators=[validate_max_calories]
    )
    notes = models.TextField(blank=True)
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Rate the workout (1-5)"
    )

    def __str__(self):
        return f"Log: {self.workout.name} on {self.completed_at.date()}"

    class Meta:
        ordering = ['-completed_at']
