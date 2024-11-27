# utils.py
from .models import Device, DeviceRecent

def sync_device_to_recent():
    """
    Copies data from device_device to device_recent table.
    Returns the number of records synced.
    """
    devices = Device.objects.all()
    synced_count = 0

    for device in devices:
        # Copy data to DeviceRecent
        _, created = DeviceRecent.objects.update_or_create(
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
        if created:
            synced_count += 1

    return synced_count
