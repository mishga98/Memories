from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Note

def index(request):
    return render(request, 'core/index.html')

def notes(request):
    notes = Note.objects.filter(person=request.user)
    return render(request, 'core/notes.html', {'notes' : notes})

