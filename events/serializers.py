from rest_framework import serializers
from .models import Event
from datetime import datetime

class EventSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Event
		fields = ('id', 'url', 'start_time', 'end_time', 'label', 'category', 'comments')

	start_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
	end_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")