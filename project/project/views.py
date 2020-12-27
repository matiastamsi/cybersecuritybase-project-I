import sqlite3
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from notes.models import Note

from django.contrib.auth.models import User
from myauth.models import MyUser

# FLAW 2: Use User instead of MyUser!
# It even works ready with request!
# Import now isn't necessary but here for clearness.
# So I didn't even implement MyUser here because
# we all can assume that Django's User works better!
# But if you enjoy doing configuration
# MyUser is ready to use (requires modifications)!
# Instead I would go check myauth/models.py and project/settings.py

def index(request):
    notes = {}
    if request.user.is_authenticated:
        notes = Note.objects.filter(owner_name= request.user.username)
    return render(request,'home.html', {'notes' : notes})

@login_required
def add_note(request):
    Note.objects.create(owner_name= request.user, note= request.POST.get('note'))
    return redirect(index)

@login_required
def search_note(request):
    searched_notes = {}
    if request.user.is_authenticated:
        # FLAW 1: SOS raw SQL queries!!
        #(<- remove to test) query = 'SELECT * FROM note WHERE owner_name LIKE "'+ request.user.username +'" and note LIKE "%' + request.POST.get('note') + '%"'
        #(<- remove to test) searched_notes = Note.objects.raw(query)
        # SQL-INJECTION (when added to 'Search'): IbetThisWordWontExist'%" UNION SELECT * FROM note WHERE "%" = "
        # Instead use covered functions no raw SQL-queries
        searched_notes = Note.objects.filter(owner_name= request.user.username, note__contains= request.POST.get('note'))
    return render(request,'home.html', {'searched_notes' : searched_notes})
