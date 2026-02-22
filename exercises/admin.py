from django.contrib import admin

from exercises.models import Exercise


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'max_sets', 'max_reps', 'rest_time']