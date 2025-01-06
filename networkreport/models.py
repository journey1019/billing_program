from django.core.exceptions import ValidationError
from django.db import models
from datetime import datetime, timezone
import pytz

class NetworkReport(models.Model):
    id = models.AutoField(primary_key=True)
    sp_id = models.IntegerField()
    serial_number = models.CharField(max_length=64)
    terminal_id = models.CharField(max_length=64, null=True)
    activated = models.DateTimeField(default=datetime(2000, 1, 1, 0, 0, 0, tzinfo=timezone.utc))
    sid = models.CharField(max_length=64, null=True)
    psn = models.CharField(max_length=64, null=True)
    mode = models.CharField(max_length=64)
    feature_options = models.CharField(max_length=64)
    profile_id = models.IntegerField()
    profile_name = models.CharField(max_length=64)
    profiles = models.IntegerField()
    ip_service_address = models.CharField(max_length=64, null=True)

    class Meta:
        unique_together = ("sp_id", "serial_number", "activated", "profile_id")

    def save(self, *args, **kwargs):
        if NetworkReport.objects.filter(
            sp_id = self.sp_id,
            serial_number = self.serial_number,
            activated = self.activated,
            profile_id = self.profile_id
        ).exists():
            raise ValidationError("Duplicate entry found for sp_id, serial_number, activated.")

        if not self.activated:
            self.activated = datetime(2000, 1, 1, 0, 0, 0, tzinfo=pytz.timezone("Asia/Seoul"))

        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.sp_id} - {self.serial_number} - {self.activated}"


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