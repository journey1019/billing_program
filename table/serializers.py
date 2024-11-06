"""
모델을 JSON으로 변환하기 위한 시리얼라이저를 정의
"""
from rest_framework import serializers
from .models import Cdr, NetworkReport, Account, DeviceManage, PricePlan

class CdrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cdr
        fields = '__all__'  # 모든 필드를 포함

class NetworkReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkReport
        fields = '__all__' # 모든 필드를 포함

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__' # 모든 필

class DeviceManageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceManage
        fields = '__all__' # 모든 필

class PricePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = PricePlan
        fields = '__all__' # 모든 필