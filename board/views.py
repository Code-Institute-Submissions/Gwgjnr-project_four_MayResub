from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Event
from .forms import EventForm


class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 20


class CreateEvent(View):

    def get(self, request, *args, **kwargs):

        return render(
            request,
            "event_form.html", 
            {
                "event_form": EventForm()
            }
        )
    
    def post(self, request, slug, *args, **kwargs):

        event_form = EventForm(data=request.POST)
        if event_form.is_valid():
            event_form.instance.email = request.user.email
            event_form.instance.author = request.user.username

            event.save()
        else:
            event_form = EventForm()

        return render(
            request, 'index.html'
        )
