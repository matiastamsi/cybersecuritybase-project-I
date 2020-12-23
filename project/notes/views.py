from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Note

def index(request):
    return render(request, 'notes/index.html')
