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
    serial_number = models.CharField(max_length=64, primary_key=True)
    region = models.CharField(max_length=10, null=True)
    amount = models.IntegerField()
    date = models.DateField(default="2000-01-01") # 기본값 추가
    date_index = models.CharField(max_length=10, default="2000-01")

    # class Meta:
    #     db_table = 'cdr'
    #     managed = False

    class Meta:
        db_table = 'cdr'
        managed = False
        constraints = [
            models.UniqueConstraint(
                fields=['datestamp', 'd_product', 'serial_number'], name='unique_cdr')
        ]


    def __str__(self):
        return f"CDR {self.record_id} - {self.record_type}"

# Network Report Table
class NetworkReport(models.Model):
    sp_id = models.IntegerField()
    serial_number = models.CharField(max_length=64, primary_key=True)
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


    class Meta:
        db_table = 'nr'
        managed = False
        constraints = [
            models.UniqueConstraint(
                fields=['sp_id', 'serial_number', 'activated'], name='unique_network')
        ]

    def __str__(self):
        return f"Network Report {self.sp_id} - {self.serial_number}"


class Account(models.Model):
    # acct_num = models.CharField(max_length=64, primary_key=True)
    acct_num = models.CharField(max_length=64, primary_key=True)
    acct_name = models.CharField(max_length=64)
    acct_residentnum = models.BigIntegerField()  # BIGINT에 대응
    classification = models.CharField(max_length=64)
    invoice_address = models.CharField(max_length=100)
    invoice_address_2 = models.CharField(max_length=100)
    invoice_postcode = models.BigIntegerField()  # BIGINT에 대응

    class Meta:
        db_table = 'account'
        managed = False

    def __str__(self):
        return f"Account {self.acct_num} - {self.acct_name}"


class DeviceManage(models.Model):
    device_manage_id = models.CharField(max_length=64, primary_key=True)
    acct_num = models.CharField(max_length=100)
    profile_id = models.IntegerField()
    serial_number = models.CharField(max_length=64)
    activated = models.DateField()
    deactivated = models.DateField()
    ppid = models.IntegerField()
    modal_name = models.CharField(max_length=64)
    internet_mail_id = models.CharField(max_length=100)
    alias = models.CharField(max_length=100, null=True, blank=True)  # NULL 허용
    remarks = models.CharField(max_length=100, null=True, blank=True)  # NULL 허용


    class Meta:
        db_table = 'device'
        managed = False
        constraints = [
            models.UniqueConstraint(
                fields=['device_manage_id', 'activated'], name='unique_device')
        ]

    def __str__(self):
        return f"DeviceManage {self.device_manage_id} - Activated: {self.activated}"


class PricePlan(models.Model):
    ppid = models.IntegerField(primary_key=True)  # Primary Key 설정
    basic_fee = models.IntegerField()
    subscription_fee = models.IntegerField()
    free_byte = models.IntegerField()
    surcharge_unit = models.IntegerField()
    each_surcharge_fee = models.FloatField()  # DOUBLE PRECISION에 대응
    apply_company = models.CharField(max_length=64)
    remarks = models.CharField(max_length=100)
    note = models.CharField(max_length=100)

    class Meta:
        db_table = 'pplan'
        managed = False
    def __str__(self):
        return f"PricePlan {self.ppid} - Company: {self.apply_company}"