""" 모델을 JSON으로 변환하기 위한 시리얼라이저를 정의 """
from rest_framework import serializers
from .models import CDR, CDRSummary

class CDRSerializer(serializers.ModelSerializer):
    class Meta:
        model = CDR
        fields = '__all__' # 모든 필드 포함

class CDRSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = CDRSummary
        fields = ['date_stamp', 'discount_code', 'd_product', 'volume_units', 'profile_id',
                  'serial_number', 'amount', 'date_only', 'date_index']