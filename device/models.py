from os import device_encoding

from django.core.exceptions import ValidationError
from django.db import models

class Device(models.Model):
    device_manage_id = models.CharField(max_length=100, primary_key=True)
    acct_num = models.CharField(max_length=10)
    profile_id = models.IntegerField()
    serial_number = models.CharField(max_length=64)
    activated = models.DateField()
    deactivated = models.DateField(null=True, blank=True)
    ppid = models.IntegerField()
    modal_name = models.CharField(max_length=64, null=True, blank=True)
    internet_mail_id = models.CharField(max_length=100, null=True, blank=True)
    alias = models.CharField(max_length=100, null=True, blank=True)  # NULL 허용
    remarks = models.CharField(max_length=100, null=True, blank=True)  # NULL 허용

    class Meta:
        unique_together = ("device_manage_id", "activated")

    def save(self, *args, **kwargs):
        if Device.objects.filter(device_manage_id=self.device_manage_id, activated=self.activated).exists():
            raise ValidationError("Duplicate entry found for device_manage_id, activated")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.device_manage_id, self.activated


class DeviceRecent(models.Model):
    device_manage_id = models.CharField(max_length=100, primary_key=True)
    acct_num = models.CharField(max_length=10)
    profile_id = models.IntegerField()
    serial_number = models.CharField(max_length=64)
    activated = models.DateField()
    deactivated = models.DateField(null=True, blank=True)
    ppid = models.IntegerField()

    def __str__(self):
        return self.device_manage_id