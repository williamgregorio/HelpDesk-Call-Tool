from rest_framework import serializers
from .models import Log

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ('id','name','call_back_number','email','problem','solution','incident_number','created_at')
