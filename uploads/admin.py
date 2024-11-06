from django.contrib import admin
from .models import CDR

@admin.register(CDR)
class CDRAdmin(admin.ModelAdmin):
    list_display = ("serial_number", "datestamp", "d_product", "amount")
    search_fields = ("serial_number", "datestamp", "d_product")
    list_filter = ("date", "date_index")
