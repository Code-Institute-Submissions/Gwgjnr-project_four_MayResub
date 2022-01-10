from .models import Event
from django import forms


class EventForm(forms.ModelForm):
    '''
    This class is used for generating my form on the event_form.html page using Crispy Forms.
    '''
    class Meta:
        model = Event
        fields = ('title', 'slug', 'summary', 'location', 'requirements', 'event_start', 'spots',)

        labels = {
            'title': 'Page title',
            'slug': 'Slug (Enter your title without spaces)',
            'summary': 'Event description',
            'location': 'location',
            'requirements': 'Requirements',
            'event_start': 'Event time and date (DD-MM-YY HH:MM)',
            'spots': 'Spaces available'
        }
