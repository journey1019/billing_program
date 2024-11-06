from rest_framework import generics
from django.shortcuts import render, redirect
from .models import Cdr, NetworkReport, Account, DeviceManage, PricePlan
from .serializers import CdrSerializer, NetworkReportSerializer, AccountSerializer, DeviceManageSerializer, PricePlanSerializer

# def table(request):
#     cdrs = Cdr.objects.all()  # 모든 CDR 데이터 가져오기
#     network_reports = NetworkReport.objects.all()
#     accounts = Account.objects.all()
#     devices = DeviceManage.objects.all()
#     priceplans = PricePlan.objects.all()
#     return render(request, 'home/home.html', {'cdrs': cdrs, 'network_reports': network_reports, 'accounts': accounts, 'devices':devices, 'priceplans': priceplans})

def table(request):
    return render(request, 'home/home.html')

class CDRListCreateAPIView(generics.ListCreateAPIView):
    queryset = Cdr.objects.all()
    serializer_class = CdrSerializer

class NetworkReportListCreateAPIView(generics.ListCreateAPIView):
    queryset = NetworkReport.objects.all()
    serializer_class = NetworkReportSerializer

class AccountListCreateAPIView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class DeviceListCreateAPIView(generics.ListCreateAPIView):
    queryset = DeviceManage.objects.all()
    serializer_class = DeviceManageSerializer

class PricePlanListCreateAPIView(generics.ListCreateAPIView):
    queryset = PricePlan.objects.all()
    serializer_class = PricePlanSerializer

