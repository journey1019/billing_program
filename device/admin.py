# admin.py
from django.contrib import admin
from .models import DeviceRecent

@admin.register(DeviceRecent)
class DeviceRecentAdmin(admin.ModelAdmin):
    list_display = ('device_manage_id', 'acct_num', 'profile_id', 'serial_number', 'activated', 'deactivated', 'ppid')
