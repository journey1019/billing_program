from django.contrib import admin
from .models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('acct_num', 'acct_name', 'classification')
    search_fields = ('acct_num', 'acct_name')
