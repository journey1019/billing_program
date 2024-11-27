from django.core.management.base import BaseCommand
from device.models import Device, DeviceRecent

class Command(BaseCommand):
    help = "Migrate data from device_device to device_recent"

    def handle(self, *args, **kwargs):
        # 기존 Device 테이블의 데이터 가져오기
        devices = Device.objects.all()

        # 중복 제거된 데이터를 device_recent 테이블에 삽입
        for device in devices:
            DeviceRecent.objects.update_or_create(
                device_manage_id=device.device_manage_id,
                activated=device.activated,
                defaults={
                    'acct_num': device.acct_num,
                    'profile_id': device.profile_id,
                    'serial_number': device.serial_number,
                    'deactivated': device.deactivated,
                    'ppid': device.ppid,
                }
            )

        self.stdout.write(self.style.SUCCESS('Successfully migrated data to DeviceRecent.'))
