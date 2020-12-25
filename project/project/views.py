from django.shortcuts import render, redirect
from notes.models import Note

def index(request):
    notes = {}
    if request.user.is_authenticated:
        notes = Note.objects.filter(owner= request.user)
    return render(request,'home.html', {'notes' : notes})

def add_note(request):
    Note.objects.create(owner= request.user, note= request.POST.get('note'))
    return redirect(index)
