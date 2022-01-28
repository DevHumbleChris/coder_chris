from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from django.core.mail import send_mail

def HomeView(request, *args, **kwargs):
    return render(request, 'index.html', {})

def SendMail(request, *args, **kwargs):
    if not request.method == "POST":
        return HttpResponseRedirect(reverse('portfolio:home'))
    if request.method == "POST":
        subject = request.POST['subject']
        message = f"""
        Mail From: {request.POST['email']},
        {request.POST['message']}
        """
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [settings.EMAIL_HOST_USER, ]
    
    try:
        send_mail(subject, message, email_from, recipient_list)
        return render(request, "thank-you.html", {
            "message": "Mail Successfully Sent!"
        })
    except Exception  as e:
        return render(request, "thank-you.html", {
            "error": e
        })
