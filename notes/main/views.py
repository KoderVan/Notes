from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django import forms
from .forms import CreateNewNote
from django.views import generic
from .models import Notes


def home(request):
    return render(request, "pages/home.html", {})


def sign_up(request):
    return render(request, "pages/sign_up_form.html", {})


def login(request):
    print("hello")
    return render(request, "pages/login.html", {})


def notes(request):
    note = Notes
    template_name = "pages/notes.html"
    return render(request, template_name, {note:"note"})


# def create_note(response):
#     note = CreateNewNote(response)
#     if note.is_valid():
#         new_note = note.cleaned_data["name"]
#         note_name = MyNotes(name=new_note)
#     return HttpResponseRedirect("/%i" % note_name)