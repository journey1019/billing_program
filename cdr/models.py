from django.core.exceptions import ValidationError
from django.db import models
from datetime import datetime, timezone
import pytz

class CDR(models.Model):
    id = models.AutoField(primary_key=True)
    record_type = models.CharField(max_length=3)
    record_id = models.IntegerField()
    datestamp = models.CharField(max_length=100)
    transaction_type = models.CharField(max_length=3)
    discount_code = models.CharField(max_length=5)
    d_product = models.CharField(max_length=10)
    msg_id = models.BigIntegerField()
    volume_unit_type = models.CharField(max_length=3)
    volume_units = models.IntegerField()
    access_id = models.CharField(max_length=100, null=True)
    profile_id = models.IntegerField()
    serial_number = models.CharField(max_length=64)
    region = models.CharField(max_length=10, null=True)
    amount = models.IntegerField()

    # Auto-generated fields based on `datestamp`
    date = models.CharField(max_length=100)
    date_index = models.CharField(max_length=100)

    class Meta:
        # Unique constraint to avoid duplicates
        unique_together = ("serial_number", "datestamp", "d_product", "msg_id")

    def save(self, *args, **kwargs):
        # Check for duplicates based on constraints
        if CDR.objects.filter(
            serial_number = self.serial_number,
            datestamp = self.datestamp,
            d_product = self.d_product,
            msg_id = self.msg_id
        ).exists():
            raise ValidationError("Duplicate entry found for serial_number, datestamp, d_product, and msg_id.")

        # Convert datestamp to datetime object
        if self.datestamp:
            try:
                # Assuming datestamp format is "YYYY-MM-DD HH:MM:SS"
                datestamp_obj = datetime.strptime(self.datestamp, "%Y-%m-%d %H:%M:%S")

                # Convert to timezone-aware datetime (UTC first)
                # datestamp_obj = timezone.make_aware(datestamp_obj, timezone.utc)
                # Convert to KST (UTC+9)
                # kst_datestamp = datestamp_obj.astimezone(timezone.pytz.timezone('Asia/Seoul'))

                # Automatically set `date` and `date_index` based on `datestamp`
                self.date = datestamp_obj.date().strftime("%Y-%m-%d")  # "YYYY-MM-DD"
                self.date_index = datestamp_obj.strftime("%Y%m")  # "YYYYMM"
            except ValueError:
                # Handle the error if the date format is incorrect
                raise ValidationError("Invalid datestamp format. Expected 'YYYY-MM-DD HH:MM:SS'.")
                # pass

        super().save(*args, **kwargs)


class CDRSummary(models.Model):
    datestamp = models.CharField(max_length=100)
    discount_code = models.CharField(max_length=5)
    d_product = models.CharField(max_length=10)
    volume_units = models.IntegerField()
    profile_id = models.IntegerField()
    serial_number = models.CharField(max_length=64)
    amount = models.IntegerField()
    date = models.CharField(max_length=100)
    date_index = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.serial_number} - {self.datestamp}"


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