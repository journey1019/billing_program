from django.core.exceptions import ValidationError
from django.db import models

class Pplan(models.Model):
    ppid = models.IntegerField(primary_key=True, unique=True)  # Primary Key 설정
    basic_fee = models.IntegerField()
    subscription_fee = models.IntegerField()
    free_byte = models.IntegerField()
    surcharge_unit = models.IntegerField()
    each_surcharge_fee = models.FloatField()  # DOUBLE PRECISION에 대응
    apply_company = models.CharField(max_length=64)
    remarks = models.CharField(max_length=100)
    note = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if Pplan.objects.filter(ppid=self.ppid).exists():
            raise ValidationError("Duplicate entry found for ppid")
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.ppid)