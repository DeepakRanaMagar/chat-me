from django.shortcuts import render, redirect

def lobby(request):
    return render(request, 'chat/lobby.html')