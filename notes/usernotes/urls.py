from django.urls import path
from .views import notes, create_note

urlpatterns = [
    path('', notes, name='note_list'),
    path('create', create_note, name='note_create')
]
