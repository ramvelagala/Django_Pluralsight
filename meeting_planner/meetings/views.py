from django.shortcuts import render, get_object_or_404, redirect
from .models import Meeting, Room
from django.forms import modelform_factory
# Create your views here.

def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})

def show_room_objects(request):
    rooms = Room.objects.all()
    return render(request, "meetings/listrooms.html", {"rooms": rooms})

#here meetingform is a class, not a object.
MeetingForm  = modelform_factory(Meeting, exclude=[])

def new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid(): # see whether the user has given valid data.
            form.save()
            return redirect("HomePage")
    else:
        form = MeetingForm()
    return render(request, "meetings/new.html", {"form": form})

