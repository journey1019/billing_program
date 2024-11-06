from django.db import models
from datetime import datetime

class CDR(models.Model):
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
    serial_number = models.CharField(max_length=64, primary_key=True)
    region = models.CharField(max_length=10, null=True)
    amount = models.IntegerField()

    # Auto-generated fields based on `datestamp`
    date = models.CharField(max_length=100)
    date_index = models.CharField(max_length=100)

    class Meta:
        # Unique constraint to avoid duplicates
        unique_together = ("serial_number", "datestamp", "d_product", "msg_id")

    def save(self, *args, **kwargs):
        # Convert datestamp to datetime object
        if self.datestamp:
            try:
                # Assuming datestamp format is "YYYY-MM-DD HH:MM:SS"
                datestamp_obj = datetime.strptime(self.datestamp, "%Y-%m-%d %H:%M:%S")

                # Automatically set `date` and `date_index` based on `datestamp`
                self.date = datestamp_obj.date().strftime("%Y-%m-%d")  # "YYYY-MM-DD"
                self.date_index = datestamp_obj.strftime("%Y%m")  # "YYYYMM"
            except ValueError:
                # Handle the error if the date format is incorrect
                pass

        super().save(*args, **kwargs)
