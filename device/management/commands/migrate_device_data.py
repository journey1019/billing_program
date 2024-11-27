# device/management/commands/migrate_device_data.py
from django.core.management.base import BaseCommand
from device.models import Device, DeviceRecent

class Command(BaseCommand):
    help = 'Migrate data from Device to DeviceRecent with deduplication'

    def handle(self, *args, **kwargs):
        # 기존 Device 데이터 가져오기
        devices = Device.objects.all()

        # 중복 제거 로직
        unique_devices = {}
        for device in devices:
            key = (device.device_manage_id, device.activated)
            if key not in unique_devices:
                unique_devices[key] = device
            else:
                # 같은 device_manage_id와 activated가 있다면 더 최신 데이터를 선택
                if device.deactivated and (not unique_devices[key].deactivated or device.deactivated > unique_devices[key].deactivated):
                    unique_devices[key] = device

        # DeviceRecent 테이블에 삽입
        for device in unique_devices.values():
            DeviceRecent.objects.create(
                device_manage_id=device.device_manage_id,
                acct_num=device.acct_num,
                profile_id=device.profile_id,
                serial_number=device.serial_number,
                activated=device.activated,
                deactivated=device.deactivated,
                ppid=device.ppid
            )

        self.stdout.write(self.style.SUCCESS('Successfully migrated data to DeviceRecent'))
