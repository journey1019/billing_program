from django.db import models

class BillingDataView(models.Model):
    datestamp = models.DateField(primary_key=True)
    discount_code = models.CharField(max_length=255)
    d_product = models.CharField(max_length=255)
    volume_units = models.IntegerField()
    profile_id = models.IntegerField()
    serial_number = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    date_index = models.CharField(max_length=6)  # YYYYMM 형식으로 저장된다고 가정
    acct_num = models.CharField(max_length=255)
    acct_resident_num = models.CharField(max_length=255)
    basic_fee = models.DecimalField(max_digits=10, decimal_places=2)
    subscription_fee = models.DecimalField(max_digits=10, decimal_places=2)
    free_byte = models.IntegerField()
    surcharge_unit = models.IntegerField()
    each_surcharge_fee = models.DecimalField(max_digits=10, decimal_places=2)
    apply_company = models.CharField(max_length=255)
    remarks = models.TextField()
    note = models.TextField()

    class Meta:
        managed = False  # 이 모델은 DB에서 직접 관리되는 뷰이므로 False로 설정
        db_table = 'billing_data_view'  # 뷰 테이블명 지정



class Account(models.Model):
    acct_num = models.CharField(max_length=10, primary_key=True)
    acct_name = models.CharField(max_length=100)
    acct_resident_num = models.BigIntegerField(null=True, blank=True)
    classification = models.CharField(max_length=100)
    invoice_address = models.CharField(max_length=100, null=True, blank=True)
    invoice_address2 = models.CharField(max_length=100, null=True, blank=True)
    invoice_postcode = models.IntegerField(null=True, blank=True)


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
