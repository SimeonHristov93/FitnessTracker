from django.core.exceptions import ValidationError
from django.utils import timezone

def validate_no_future_date(value):
    if value > timezone.now():
        raise ValidationError("The date cannot be in the future.")

def validate_max_calories(value):
    if value > 5000:
        raise ValidationError("Calories burned cannot exceed 5000.")

def validate_max_duration(value):
    if value > 360:
        raise ValidationError("Duration cannot exceed 6 hours (360 minutes).")
