import sqlite3
from django.shortcuts import render, redirect
from notes.models import Note

def index(request):
    notes = {}
    if request.user.is_authenticated:
        notes = Note.objects.filter(owner_name= request.user.username)
    return render(request,'home.html', {'notes' : notes})

def add_note(request):
    Note.objects.create(owner_name= request.user, note= request.POST.get('note'))
    return redirect(index)

def search_note(request):
    searched_notes = {}
    if request.user.is_authenticated:
        #SOS raw SQL queries!!
        #query = 'SELECT * FROM note WHERE owner_name LIKE "'+ request.user.username +'" and note LIKE "%' + request.POST.get('note') + '%"'
        #searched_notes = Note.objects.raw(query)
        # SQL-INJECTION (when added to 'Search'): IbetThisWordWontExist'%" UNION SELECT * FROM note WHERE owner_name=owner_name or owner_name ="
        # Instead use covered functions no raw SQL-queries
        searched_notes = Note.objects.filter(owner_name= request.user.username, note__contains= request.POST.get('note'))
    return render(request,'home.html', {'searched_notes' : searched_notes})
