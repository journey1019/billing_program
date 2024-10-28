from django.db import models

# CDR Table
class Cdr(models.Model):
    record_type = models.CharField(max_length=3)
    record_id = models.IntegerField()
    datestamp = models.DateTimeField()
    transaction_type = models.CharField(max_length=3)
    discount_code = models.CharField(max_length=5)
    d_product = models.CharField(max_length=10)
    msg_id = models.BigIntegerField()
    volume_unit_type = models.CharField(max_length=3)
    volume_units = models.IntegerField()
    access_id = models.CharField(max_length=100, null=True)
    profile_id = models.IntegerField()
    mobile_id = models.CharField(max_length=64)
    region = models.CharField(max_length=10, null=True)
    amount = models.IntegerField()

    def __str__(self):
        return f"CDR {self.record_id} - {self.record_type}"

# Network Report Table
class NetworkReport(models.Model):
    sp_id = models.IntegerField()
    serial_number = models.CharField(max_length=64)
    terminal_id = models.CharField(max_length=64, null=True)
    activated = models.DateTimeField(null=True, blank=True)  # NULL 허용
    sid = models.CharField(max_length=64, null=True)
    psn = models.CharField(max_length=64, null=True)
    mode = models.CharField(max_length=64)
    feature_options = models.CharField(max_length=64)
    profile_id = models.IntegerField()
    profile_name = models.CharField(max_length=64)
    profiles = models.IntegerField()
    ip_service_address = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"Network Report {self.sp_id} - {self.serial_number}"
