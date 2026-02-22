from django import forms
from .models import Workout


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['name', 'description', 'workout_type', 'duration_minutes', 'difficulty']
        widgets = {
            'description': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Describe the workout (Exercises and Sets)',
                'class': 'form-control'
            }),
            'name': forms.TextInput(attrs={
                'placeholder': 'e.g., Full Body, Cardio, High Intensity Training',
                'class': 'form-control'
            }),

        }
        help_texts = {
            'duration_minutes': 'Workout duration in minutes (5-300)',
            'difficulty': 'Select appropriate difficulty level',
        }
        labels = {
            'duration_minutes': 'Duration (minutes)',
        }

    def clean_duration_minutes(self):
        duration = self.cleaned_data['duration_minutes']
        if duration < 5:
            raise forms.ValidationError("Workout must be at least 5 minutes.")
        if duration > 300:
            raise forms.ValidationError("Workout cannot exceed 300 minutes.")
        return duration