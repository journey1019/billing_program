### CSV 파일에서 데이터가 저장될 모델 정의
from django.db import models

# 예시 세팅 데이터 모델 정의
class DataRecord(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()
    # 추가 필드 정의

    def __str__(self):
        return f"{self.field1}, {self.field2}"

# 'cdr' 테이블을 위한 모델 정의
class CDR(models.Model):
    RECORD_TYPE = models.CharField(max_length=3)
    RECORD_ID = models.IntegerField()
    DATESTAMP = models.DateTimeField()
    TRANSACTION_TYPE = models.CharField(max_length=3)
    DISCOUNT_CODE = models.CharField(max_length=5)
    D_PRODUCT = models.CharField(max_length=10)
    MSG_ID = models.BigIntegerField()
    VOLUME_UNIT_TYPE = models.CharField(max_length=3)
    VOLUME_UNITS = models.IntegerField()
    ACCESS_ID = models.CharField(max_length=100)
    PROFILE_ID = models.IntegerField()
    MOBILE_ID = models.CharField(max_length=64)
    REGION = models.CharField(max_length=10)
    AMOUNT = models.IntegerField()
    FIELD_TYPE = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.RECORD_ID} - {self.MOBILE_ID}"


