from datetime import time
from django.db import models

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=50)
    floor_nr = models.IntegerField(default=0)
    room_nr = models.IntegerField()

    def __str__(self):
        return f'{self.name}: room {self.room_nr} floor {self.floor_nr}'


class Meeting(models.Model):
    title = models.CharField(max_length=200)
    data = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} will start at {self.start_time} on {self.data} and will last for {self.duration} h'
