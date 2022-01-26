from django.shortcuts import render

def HomeView(request, *args, **kwargs):
    return render(request, 'index.html', {})