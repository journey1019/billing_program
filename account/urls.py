from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AccountList, AccountCreate, AccountViewSet

app_name = 'account'

router = DefaultRouter()
router.register(r'account_data', AccountViewSet, basename="account")

urlpatterns = [
    path('', AccountList, name='account_list'),
    path('create/', AccountCreate, name='account_create'),

    path("api/", include(router.urls)),
]
