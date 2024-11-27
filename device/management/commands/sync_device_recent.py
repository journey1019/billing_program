from django.core.management.base import BaseCommand
from device.utils import sync_device_to_recent


class Command(BaseCommand):
    help = 'Sync data from device_device to device_recent table'

    def handle(self, *args, **kwargs):
        synced_count = sync_device_to_recent()
        self.stdout.write(self.style.SUCCESS(f'{synced_count} records synced to device_recent.'))
