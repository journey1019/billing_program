from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PplanList, PplanCreate, PplanViewSet

app_name = 'pplan'

router = DefaultRouter()
router.register(r'pplan_data', PplanViewSet, basename="pplan")

urlpatterns = [
    path('', PplanList, name='pplan_list'),
    path('create/', PplanCreate, name='pplan_create'),

    path("api/", include(router.urls)),
]
