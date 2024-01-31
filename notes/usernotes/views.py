from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Note
from .forms import Noteform
from django.contrib.auth.decorators import login_required


def notes(request):
    note = Note.objects.all()
    template_name = "pages/notes.html"
    return render(request, template_name, {"notes": note})


@login_required
def create_note(request):
    if request.method == 'POST':
        form = Noteform(request.POST)
        if form.is_valid():
            note = form.cleaned_data['title']
            t = Noteform(title=note)
            note.save()
            request.user.Note.add(t)
            return redirect('notes')
    else:
        form = Noteform()
    return render(request, "pages/create_note.html", {'form': form})
