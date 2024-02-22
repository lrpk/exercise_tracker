from django import forms
from django.core.exceptions import ValidationError


def validate_integer(value):
    if not isinstance(value, int):
        raise ValidationError


class ExerciseForm(forms.Form):
    push_ups = forms.IntegerField(validators=[validate_integer], required=True)
    sit_ups = forms.IntegerField(validators=[validate_integer], required=True)
    squads = forms.IntegerField(validators=[validate_integer], required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields.keys():
            self.fields[field_name].widget.attrs['class'] = 'reps'
