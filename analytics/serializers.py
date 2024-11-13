from rest_framework import serializers
from cdr.models import CDR
from device.models import Device
from account.models import Account
from pplan.models import Pplan

class CdrDeviceDataSerializer(serializers.ModelSerializer):
    acct_num = serializers.SerializerMethodField()
    acct_name = serializers.SerializerMethodField()
    ppid = serializers.SerializerMethodField()
    basic_fee = serializers.SerializerMethodField()
    subscription_fee = serializers.SerializerMethodField()
    free_byte = serializers.SerializerMethodField()
    surcharge_unit = serializers.SerializerMethodField()
    each_surcharge_fee = serializers.SerializerMethodField()
    apply_company = serializers.SerializerMethodField()
    remarks = serializers.SerializerMethodField()
    note = serializers.SerializerMethodField()

    class Meta:
        model = CDR
        fields = [
            'id', 'record_type', 'record_id', 'datestamp', 'transaction_type',
            'discount_code', 'd_product', 'msg_id', 'volume_unit_type', 'volume_units',
            'access_id', 'profile_id', 'serial_number', 'region', 'amount', 'date',
            'date_index', 'acct_num', 'acct_name', 'ppid',
            'basic_fee', 'subscription_fee', 'free_byte', 'surcharge_unit',
            'each_surcharge_fee', 'apply_company', 'remarks', 'note'
        ]

    def get_acct_num(self, obj):
        # CDR의 serial_number와 매칭되는 Device의 acct_num을 가져옴
        try:
            device = Device.objects.get(serial_number=obj.serial_number)
            return device.acct_num
        except Device.DoesNotExist:
            return None

    def get_acct_name(self, obj):
        # acct_num을 통해 Account의 acct_name을 가져옴
        acct_num = self.get_acct_num(obj)
        if acct_num:
            try:
                account = Account.objects.get(acct_num=acct_num)
                return account.acct_name
            except Account.DoesNotExist:
                return None
        return None

    def get_ppid(self, obj):
        # CDR의 serial_number와 매칭되는 Device의 ppid를 가져옴
        try:
            device = Device.objects.get(serial_number=obj.serial_number)
            return device.ppid
        except Device.DoesNotExist:
            return None

    def get_basic_fee(self, obj):
        ppid = self.get_ppid(obj)
        if ppid:
            try:
                pplan = Pplan.objects.get(ppid=ppid)
                return pplan.basic_fee
            except Pplan.DoesNotExist:
                return None
        return None

    # 각 pplan의 필드에 대해 동일한 방식으로 추가
    def get_subscription_fee(self, obj):
        ppid = self.get_ppid(obj)
        if ppid:
            try:
                pplan = Pplan.objects.get(ppid=ppid)
                return pplan.subscription_fee
            except Pplan.DoesNotExist:
                return None
        return None

    def get_free_byte(self, obj):
        ppid = self.get_ppid(obj)
        if ppid:
            try:
                pplan = Pplan.objects.get(ppid=ppid)
                return pplan.free_byte
            except Pplan.DoesNotExist:
                return None
        return None

    def get_surcharge_unit(self, obj):
        ppid = self.get_ppid(obj)
        if ppid:
            try:
                pplan = Pplan.objects.get(ppid=ppid)
                return pplan.surcharge_unit
            except Pplan.DoesNotExist:
                return None
        return None

    def get_each_surcharge_fee(self, obj):
        ppid = self.get_ppid(obj)
        if ppid:
            try:
                pplan = Pplan.objects.get(ppid=ppid)
                return pplan.each_surcharge_fee
            except Pplan.DoesNotExist:
                return None
        return None

    def get_apply_company(self, obj):
        ppid = self.get_ppid(obj)
        if ppid:
            try:
                pplan = Pplan.objects.get(ppid=ppid)
                return pplan.apply_company
            except Pplan.DoesNotExist:
                return None
        return None

    def get_remarks(self, obj):
        ppid = self.get_ppid(obj)
        if ppid:
            try:
                pplan = Pplan.objects.get(ppid=ppid)
                return pplan.remarks
            except Pplan.DoesNotExist:
                return None
        return None

    def get_note(self, obj):
        ppid = self.get_ppid(obj)
        if ppid:
            try:
                pplan = Pplan.objects.get(ppid=ppid)
                return pplan.note
            except Pplan.DoesNotExist:
                return None
        return None
