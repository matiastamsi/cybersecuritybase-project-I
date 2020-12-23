from django.shortcuts import render

def login(request):
    request.user.login()

def logout(request):
    request.user.logout()

