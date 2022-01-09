from . import views
from django.urls import path


urlpatterns = [
    path('', views.EventList.as_view(), name='home'),
    path('create_event/', views.CreateEvent.as_view(), name='create_event'),
    path('join/<slug:slug>', views.JoinEvent.as_view(), name='join_event'),
    path('delete/<slug:slug>', views.DeleteEvent.as_view(), name='delete_event'),
]
