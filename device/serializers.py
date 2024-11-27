from rest_framework import serializers
from .models import Device, DeviceRecent

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

class DeviceRecentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceRecent
        fields = '__all__'