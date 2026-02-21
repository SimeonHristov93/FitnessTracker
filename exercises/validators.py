from django.core.exceptions import ValidationError

def validate_rest_time(value):
    if value > 600:  # 10 minutes in seconds
        raise ValidationError("Rest time cannot exceed 10 minutes (600 seconds).")

def validate_name_length(value):
    if len(value) < 3:
        raise ValidationError("Name must be at least 3 characters long.")

def validate_max_reps(value):
    if value > 100:
        raise ValidationError("Repetitions cannot exceed 100.")

def validate_max_sets(value):
    if value > 20:
        raise ValidationError("Sets cannot exceed 20.")
