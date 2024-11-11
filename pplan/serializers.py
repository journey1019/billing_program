from rest_framework import serializers
from .models import Pplan

class PplanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pplan
        fields = '__all__'