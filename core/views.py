from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Note
from .forms import NoteForm
def index(request):
    return render(request, 'core/index.html')

def notes(request):
    if request.method == 'POST':
        request.POST = request.POST.copy()
        request.POST['person']=request.user
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes')
    form = NoteForm()
    notes = Note.objects.filter(person=request.user)
    context = {
        'form': form,
        'notes': notes
    }
    return render(request, 'core/notes.html', context)

