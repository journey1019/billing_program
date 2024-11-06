from django.db import models
from django.utils import timezone

class CDR(models.Model):
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
    serial_number = models.CharField(max_length=64, primary_key=True)
    region = models.CharField(max_length=10, null=True)
    amount = models.IntegerField()

    # Auto-generated fields based on `datestamp`
    date = models.DateField(editable=False)
    date_index = models.CharField(max_length=6, editable=False)

    class Meta:
        # Unique constraint to avoid duplicates
        unique_together = ("serial_number", "datestamp", "d_product", "msg_id")

    def save(self, *args, **kwargs):
        # Automatically set `date` and `date_index` based on `datestamp`
        self.date = self.datestamp.date()
        self.date_index = self.datestamp.strftime("%Y%m")
        super().save(*args, **kwargs)
