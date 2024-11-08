from django.core.exceptions import ValidationError
from django.db import models


class Account(models.Model):
    acct_num = models.CharField(max_length=10, primary_key=True)
    acct_name = models.CharField(max_length=100)
    acct_resident_num = models.BigIntegerField(null=True)
    classification = models.CharField(max_length=100)
    invoice_address = models.CharField(max_length=100, null=True)
    invoice_address2 = models.CharField(max_length=100, null=True)
    invoice_postcode = models.IntegerField(null=True)

    class Meta:
        unique_together = ("acct_num",)

    def save(self, *args, **kwargs):
        if Account.objects.filter(acct_num=self.acct_num).exists():
            raise ValidationError("Duplicate entry found for acct_num")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.acct_name
