from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework import filters

from .models import Device
from .forms import DeviceForm
from .serializers import DeviceSerializer


def DeviceList(request):
    devices = Device.objects.all()
    return render(request, 'device/device_list.html', {'devices': devices})

def DeviceCreate(request):
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '단말 정보가 성공적으로 생성되었습니다.')
            return redirect('device:device_list')
    else:
        form = DeviceForm()
    return render(request, 'device/device_form.html', {'form': form})

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    pagination_class = PageNumberPagination
