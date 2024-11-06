from rest_framework import viewsets, generics
from ..models import Cdr, NetworkReport, Account, DeviceManage, PricePlan
from ..serializers import CdrSerializer, NetworkReportSerializer, AccountSerializer, DeviceManageSerializer, PricePlanSerializer

class CdrViewSet(viewsets.ModelViewSet):
    queryset = Cdr.objects.all()
    serializer_class = CdrSerializer

class NetworkReportViewSet(viewsets.ModelViewSet):
    queryset = NetworkReport.objects.all()
    serializer_class = NetworkReportSerializer

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class DeviceManageViewSet(viewsets.ModelViewSet):  # 이름 변경
    queryset = DeviceManage.objects.all()
    serializer_class = DeviceManageSerializer

class PricePlanViewSet(viewsets.ModelViewSet):
    queryset = PricePlan.objects.all()
    serializer_class = PricePlanSerializer
