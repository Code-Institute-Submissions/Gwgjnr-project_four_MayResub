from django.contrib import admin
from .models import Event
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Event)
class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('details', 'requirements')
