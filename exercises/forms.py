from django import forms

from .models import Exercise


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'description', 'muscle_group', 'equipment', 'sets', 'reps', 'rest_seconds', 'workout']
        widgets = {
            'description': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Describe the exercise and proper form...',
                'class': 'form-control'
            }),
            'name': forms.TextInput(attrs={
                'placeholder': 'e.g., Squats, Push-ups',
                'class': 'form-control'
            }),
            'rest_seconds': forms.NumberInput(attrs={
                'min': 0,
                'max': 300,
                'class': 'form-control'
            }),
            'workout': forms.Select(attrs={'class': 'form-select'}),
        }
        help_texts = {
            'rest_seconds': 'Rest time between sets (0-300 seconds)',
            'sets': 'Number of sets to perform',
            'reps': 'Repetitions per set',
        }

    def clean_rest_seconds(self):
        rest = self.cleaned_data['rest_seconds']
        if rest < 0:
            raise forms.ValidationError("Rest time cannot be negative.")
        if rest > 300:
            raise forms.ValidationError("Rest time cannot exceed 300 seconds.")
        return rest