from rest_framework import serializers
from cdr.models import CDR
from device.models import Device  # device 모델을 import합니다.

class CdrDeviceDataSerializer(serializers.ModelSerializer):
    acct_num = serializers.SerializerMethodField()
    ppid = serializers.SerializerMethodField()

    class Meta:
        model = CDR
        fields = [
            'id', 'record_type', 'record_id', 'datestamp', 'transaction_type',
            'discount_code', 'd_product', 'msg_id', 'volume_unit_type', 'volume_units',
            'access_id', 'profile_id', 'serial_number', 'region', 'amount', 'date',
            'date_index', 'acct_num', 'ppid'
        ]

    def get_acct_num(self, obj):
        # CDR의 serial_number와 매칭되는 Device의 acct_num을 가져옵니다.
        try:
            device = Device.objects.get(serial_number=obj.serial_number)
            return device.acct_num
        except Device.DoesNotExist:
            return None  # 매칭되는 Device가 없는 경우 None을 반환

    def get_ppid(self, obj):
        # CDR의 serial_number와 매칭되는 Device의 ppid를 가져옵니다.
        try:
            device = Device.objects.get(serial_number=obj.serial_number)
            return device.ppid
        except Device.DoesNotExist:
            return None
