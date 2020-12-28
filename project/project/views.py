import sqlite3
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.html import strip_tags, escape
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

@login_required    # FLAW 3.0: Must be authenticated 
def index(request):# FLAW 3.1: Provide only for user that requested
    notes = {}
    notes = Note.objects.filter(owner_name= request.user.username)
    return render(request,'home.html', {'notes' : notes})

@login_required # FLAW 3 (same apply than in comments of index())
def add_note(request):
    # FLAW 4.0: Don't allow tags and escape for html and scripts
    form_note = escape(strip_tags(request.POST.get('note')))
    Note.objects.create(owner_name= request.user, note= form_note)
    return redirect(index)

@login_required # FLAW 3 (same apply than in comments of index())
def search_note(request):
    searched_notes = {}
    # FLAW 1: SOS raw SQL queries!!
    #(<- remove to test) query = 'SELECT * FROM note WHERE owner_name LIKE "'+ request.user.username +'" and note LIKE "%' + request.POST.get('note') + '%"'
    #(<- remove to test) searched_notes = Note.objects.raw(query)
    # SQL-INJECTION (when added to 'Search'): 
    # IbetThisWordWontExist'%" UNION SELECT * FROM note WHERE "%" = "
    # FLAW 4.1: Check also query parameters! See 4.0.
    form_note = escape(strip_tags(request.POST.get('note')))
    searched_notes = Note.objects.filter(owner_name= request.user.username, note__contains= form_note)
    return render(request,'home.html', {'searched_notes' : searched_notes})
