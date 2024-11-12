from django.db import models
from django.db.models import Sum

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

    def get_total_fee(self, date_index):
        # 같은 serial_number에 대한 total_fee 계산
        total_fee = BillingDataView.objects.filter(
            serial_number=self.serial_number, date_index=date_index
        ).aggregate(Sum('amount'))['amount__sum']
        return total_fee

    def get_total_day(self, start_date, end_date):
        # 시작일과 종료일 사이의 총 일수를 계산
        delta = end_date - start_date
        return delta.days

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
