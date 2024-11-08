from rest_framework import serializers
from .models import NetworkReport

class NetworkReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkReport
        fields = '__all__'