from django import forms
from .models import WorkoutLog


class WorkoutLogForm(forms.ModelForm):
    workout_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'readonly': 'readonly',
            'class': 'form-control-plaintext'
        }),
        required=False,
    )

    rating = forms.TypedChoiceField(
        coerce=int,
        choices=[(i, f"{i} Stars") for i in range(1, 6)],
        widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = WorkoutLog
        fields = ['workout', 'completed_at', 'duration_minutes', 'calories_burned', 'notes', 'rating']
        exclude = ['workout_name']
        widgets = {
            'completed_at': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control'
            }),
            'notes': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'How did it go? Any modifications?',
                'class': 'form-control'
            }),
            'calories_burned': forms.NumberInput(attrs={
                'min': 1,
                'class': 'form-control',
                'placeholder': 'Optional'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['workout_name'].initial = self.instance.workout.name

    def clean_calories_burned(self):
        calories = self.cleaned_data.get('calories_burned')
        if calories is not None:
            try:
                calories = int(calories)
            except (ValueError, TypeError):
                raise forms.ValidationError("Enter a valid number.")

            if calories < 1:
                raise forms.ValidationError("Calories burned must be at least 1.")
        return calories
