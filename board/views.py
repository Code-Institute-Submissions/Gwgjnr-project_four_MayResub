from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from .models import Event
from .forms import EventForm
from datetime import datetime


class EventList(generic.ListView):
    '''
    This view is used for generating the event list homepage.
    '''  
    model = Event
    queryset = Event.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class CreateEvent(View):
    '''
    This view is used for generating the event_form page and saving the 
    input to create a new event item.
    '''
    def get(self, request, *args, **kwargs):

        return render(
            request,
            "event_form.html",
            {
                "event_form": EventForm()
            }
        )

    def post(self, request, *args, **kwargs):

        event_form = EventForm(data=request.POST)
        if event_form.is_valid():
            event_form.instance.email = request.user.email
            event_form.instance.author = request.user
            event_form.instance.created_on = datetime.now()
            event_form.save()
        else:
            event_form = EventForm()

        return redirect('/')


class JoinEvent(View):
    '''
    This view is used for joining or cancelling your spot at an event, it also 
    updates the available spaces each time a user changes their status.
    '''    
    def post(self, request, slug, *args, **kwargs):
        event = get_object_or_404(Event, slug=slug)
        if request.user in event.signed_up.all():
            event.signed_up.remove(request.user)
            event.spots += 1
            event.save()
        else:
            event.signed_up.add(request.user)
            event.spots -= 1
            event.save()
        return redirect('/')


class DeleteEvent(View):
    '''
    This view is used for deleting an event.
    ''' 
    def post(self, request, slug, *args, **kwargs):
        event = get_object_or_404(Event, slug=slug)
        event.delete()
        return redirect('/')
