""" 모델을 JSON으로 변환하기 위한 시리얼라이저를 정의 """
from rest_framework import serializers
from .models import CDR

class CDRSerializer(serializers.ModelSerializer):
    class Meta:
        model = CDR
        fields = '__all__' # 모든 필드 포함