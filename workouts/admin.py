from django.contrib import admin
from workouts.models import Workout



@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'workout_type', 'duration_minutes', 'difficulty']