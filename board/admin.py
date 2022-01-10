from django.contrib import admin
from .models import Event
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Event)
class PostAdmin(SummernoteModelAdmin):
    '''
    This class is used for generating my admin panel and to allow sorting through events.
    '''
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'details', 'requirements']
    list_filter = ('status', 'created_on', 'event_start')
