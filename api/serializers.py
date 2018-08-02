from rest_framework import serializers
from ranix_web.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('date', 'start_time', 'end_time')
