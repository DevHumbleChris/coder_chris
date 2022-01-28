from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

def HomeView(request, *args, **kwargs):
    return render(request, 'index.html', {})

def SendMail(request, *args, **kwargs):
    if not request.method == "POST":
        return HttpResponseRedirect(reverse('portfolio:home'))
    if request.method == "POST":
        print("post here")
        return render(request, "thank-you.html", {})
