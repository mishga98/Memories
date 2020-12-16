from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm


def index(request):
    return render(request, 'core/index.html')


def notes(request):
    if str(request.user) == 'AnonymousUser':

        return redirect('home')

    if request.method == 'POST':
        request.POST = request.POST.copy()
        request.POST['person'] = request.user
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes')
    form = NoteForm()
    mynotes = Note.objects.filter(person=request.user).order_by('-id')
    context = {
        'form': form,
        'notes': mynotes
    }
    return render(request, 'core/notes.html', context)
