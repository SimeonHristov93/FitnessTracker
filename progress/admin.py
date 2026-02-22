from django.contrib import admin

from progress.models import WorkoutLog


@admin.register(WorkoutLog)
class WorkoutLogAdmin(admin.ModelAdmin):
    fields = ['workout', 'completed_at', 'duration_minutes', 'calories_burned', 'notes', 'rating']
