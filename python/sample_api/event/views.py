from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from event.serializers import EventSerializer
from event.models import Event


class EventViewSet(ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
