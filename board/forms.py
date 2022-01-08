from .models import Event
from django import forms


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'slug', 'summary', 'location', 'requirements', 'event_start', 'spots',)
