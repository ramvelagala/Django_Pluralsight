from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from meetings.models import Meeting


def welcome(request):
    return render(request, "website/welcome.html",
                  {"meetings": Meeting.objects.all()})

def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))

def about(request):
    return HttpResponse("This is Rama Krishna reddy. My age is 26 years old.")