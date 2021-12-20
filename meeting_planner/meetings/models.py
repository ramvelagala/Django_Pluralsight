from django.db import models


# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=200, default="Cheif Warden Files")
    floor_number = models.IntegerField()
    room_number = models.IntegerField()

    def __str__(self):
        return f"{self.name}: room {self.room_number} on floor {self.floor_number}."

class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    priority = models.CharField(max_length=200, default="High")
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} on {self.date} - {self.priority} priority."


