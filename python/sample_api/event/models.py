from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=300)
    place = models.CharField(max_length=300)
    event_date = models.DateField()

    def __str__(self):
        return self.name
