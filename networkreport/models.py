from django.core.exceptions import ValidationError
from django.db import models
from datetime import datetime, timezone
import pytz

class NetworkReport(models.Model):
    id = models.AutoField(primary_key = True)
    sp_id = models.IntegerField()
    serial_number = models.CharField(max_length=64)
    terminal_id = models.CharField(max_length=64)
    activated = models.DateTimeField(default=datetime(2000,1,1,tzinfo=timezone.utc))  # 기본값 설정
    sid = models.CharField(max_length=64)
    psn = models.CharField(max_length=64)
    mode = models.CharField(max_length=64)
    feature_options = models.CharField(max_length=64)
    profile_id = models.IntegerField()
    profile_name = models.CharField(max_length=64)
    profiles = models.IntegerField()
    ip_service_address = models.CharField(max_length=64)

    class Meta:
        unique_together = ("sp_id", "serial_number", "activated")

    def save(self, *args, **kwargs):
        if NetworkReport.objects.filter(
            sp_id = self.sp_id,
            serial_number = self.serial_number,
            activated = self.activated
        ).exists():
            raise ValidationError("Duplicate entry found for sp_id, serial_number, activated.")

        # activated 필드가 비어있을 경우 기본값 설정
        if not self.activated:
            self.activated = timezone.datetime(2000, 1, 1)
        # if not self.activated:
        #     self.activated = "2000-01-01 00:00:00.000"

        super().save(*args, **kwargs)


class UploadedNRFile(models.Model):
    file_name = models.CharField(max_length=225, unique=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='networkreport/csvs/')

    def save(self, *args, **kwargs):
        # 시간대 변환 UTC -> KST
        if self.upload_date:
            kst_timezone = pytz.timezone('Asia/Seoul')
            self.upload_date == self.upload_date.astimezone(kst_timezone)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.file_name