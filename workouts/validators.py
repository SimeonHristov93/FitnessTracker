from django.core.exceptions import ValidationError

def validate_name_length(value):
    if len(value) < 3:
        raise ValidationError("Name must be at least 3 characters long.")

def validate_description_length(value):
    if len(value) < 10:
        raise ValidationError("Description must be at least 10 characters long.")
