from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from datetime import datetime, datetime_CAPI
import pytz

class CDR(models.Model):
    id = models.AutoField(primary_key=True)
    record_type = models.CharField(max_length=3)
    record_id = models.IntegerField()
    date_stamp = models.DateTimeField()
    transaction_type = models.CharField(max_length=3)
    discount_code = models.CharField(max_length=5)
    d_product = models.CharField(max_length=10)
    msg_id = models.BigIntegerField()
    volume_unit_type = models.CharField(max_length=3)
    volume_units = models.IntegerField()
    access_id = models.CharField(max_length=100, null=True, blank=True)
    profile_id = models.IntegerField()
    serial_number = models.CharField(max_length=64)
    region = models.CharField(max_length=10, null=True, blank=True)
    amount = models.IntegerField()

    # Auto-generated fields based on `date_stamp`
    date_only = models.DateField()
    date_index = models.CharField(max_length=6)

    class Meta:
        # Unique constraint to avoid duplicates
        unique_together = ("serial_number", "date_stamp", "d_product", "msg_id", "record_id")

    def save(self, *args, **kwargs):
        # Check for duplicates based on constraints
        if CDR.objects.filter(
            serial_number = self.serial_number,
            date_stamp = self.date_stamp,
            d_product = self.d_product,
            msg_id = self.msg_id,
            record_id = self.record_id
        ).exists():
            raise ValidationError("Duplicate entry found for serial_number, date_stamp, d_product, msg_id, record_id.")

        # Convert date_stamp to datetime if it's a string
        if isinstance(self.date_stamp, str):
            self.date_stamp = datetime.strptime(self.date_stamp, "%Y-%m-%d %H:%M:%S")

        self.date_stamp = self.date_stamp.replace(microsecond=0)

        #print(f"{self.date_stamp} {self.serial_number}")
        # Convert datetime to Asia/Seoul time zone
        # self.date_stamp = pytz.timezone('Asia/Seoul').localize(self.date_stamp)

        # If timezone-aware, you can make it naive (if needed) or proceed with aware datetime
        # self.date_stamp = timezone.make_naive(self.date_stamp, timezone=pytz.timezone('Asia/Seoul'))

        # self.date_stamp = datetime.strptime(self.date_stamp, "%Y-%m-%d %H:%M:%S")
        self.date_only = self.date_stamp.date()  # YYYY-MM-DD 형식
        self.date_index = self.date_stamp.strftime("%Y%m")  # YYYYMM 형식

        super().save(*args, **kwargs)
    # def __str__(self):
    #     return f"{self.serial_number} - {self.date_stamp} - {self.d_product}"



class CDRSummary(models.Model):
    date_stamp = models.DateTimeField()
    discount_code = models.CharField(max_length=5)
    d_product = models.CharField(max_length=10)
    volume_units = models.IntegerField()
    profile_id = models.IntegerField()
    serial_number = models.CharField(max_length=64)
    amount = models.IntegerField()
    date_only = models.DateField()
    date_index = models.CharField(max_length=6)

    def __str__(self):
        return f"{self.serial_number} - {self.date_stamp}"


# 업로드 된 파일 이름과 파일 경로 저장 & 중복된 파일 이름을 허용하지 안함
class UploadedFile(models.Model):
    file_name = models.CharField(max_length=225, unique=True) # 파일 이름은 고유함
    upload_date = models.DateTimeField(auto_now_add=True) # 업로드된 날짜
    file = models.FileField(upload_to='cdr/csvs/') # 업로드된 파일 경로

    def save(self, *args, **kwargs):
        # 시간대 변환: UTC -> KST
        if self.upload_date:
            kst_timezone = pytz.timezone('Asia/Seoul')
            # UTC로 저장된 시간을 KST로 변환
            self.upload_date = self.upload_date.astimezone(kst_timezone)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.file_name