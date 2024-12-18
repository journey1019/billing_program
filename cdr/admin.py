from django.contrib import admin
from .models import CDR

@admin.register(CDR)
class CDRAdmin(admin.ModelAdmin):
    list_display = ("serial_number", "date_stamp", "d_product", "msg_id", "discount_code", "volume_units", "profile_id", "amount", "date_only", "date_index")
    search_fields = ("serial_number", "date_stamp", "d_product")
    list_filter = ("date_only", "date_index")