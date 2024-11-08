from django.urls import path
from .views import account_list, account_create

app_name = 'account'

urlpatterns = [
    path('', account_list, name='account_list'),
    path('create/', account_create, name='account_create'),
]
