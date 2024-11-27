import csv
from .serializers import DeviceRecentSerializer
from datetime import datetime
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.viewsets import ReadOnlyModelViewSet
from .utils import sync_device_to_recent



from .models import Device, DeviceRecent
from .forms import DeviceForm, DeviceUploadForm
from .serializers import DeviceSerializer

def parse_date(date_str):
    """
    Helper function to parse dates in the format 'YYYY. MM. DD' to 'YYYY-MM-DD'.
    """
    try:
        return datetime.strptime(date_str.strip(), '%Y. %m. %d').strftime('%Y-%m-%d') if date_str else None
    except ValueError:
        return None

# def DeviceUpload(request):
#     if request.method == 'POST':
#         csv_file = request.FILES['csv_file']
#         decoded_file = csv_file.read().decode('utf-8').splitlines()
#         reader = csv.DictReader(decoded_file)
#
#         for row in reader:
#             try:
#                 # 날짜 형식 변환
#                 activated_date = None
#                 deactivated_date = None
#
#                 # activated 필드 형식 변환
#                 if row.get('activated'):
#                     try:
#                         activated_date = datetime.strptime(row['activated'].strip(), '%Y. %m. %d').strftime('%Y-%m-%d')
#                     except ValueError:
#                         messages.error(request, f"유효하지 않은 날짜 형식 (activated): {row['activated']}")
#                         return redirect('device:device_list')
#
#                 # deactivated 필드 형식 변환
#                 if row.get('deactivated'):
#                     try:
#                         deactivated_date = datetime.strptime(row['deactivated'].strip(), '%Y. %m. %d').strftime('%Y-%m-%d')
#                     except ValueError:
#                         messages.error(request, f"유효하지 않은 날짜 형식 (deactivated): {row['deactivated']}")
#                         return redirect('device:device_list')
#
#                 # Device 객체 생성
#                 device = Device(
#                     device_manage_id=row['device_manage_id'],
#                     acct_num=row['acct_num'],
#                     profile_id=row['profile_id'],
#                     serial_number=row['serial_number'],
#                     activated=activated_date,
#                     deactivated=deactivated_date,
#                     ppid=row['ppid'],
#                     modal_name=row.get('modal_name', ''),
#                     internet_mail_id=row.get('internet_mail_id', ''),
#                     alias=row.get('alias', ''),
#                     remarks=row.get('remarks', '')
#                 )
#                 device.save()
#
#             except ValidationError as e:
#                 messages.error(request, f"데이터 검증 오류: {e}")
#                 return redirect('device:device_list')
#
#         messages.success(request, 'CSV 파일이 성공적으로 업로드되었습니다.')
#         return redirect('device:device_list')
def DeviceUpload(request):
    if request.method == 'POST':
        csv_file = request.FILES['csv_file']
        decoded_file = csv_file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)

        devices_to_create = []
        errors = []
        for row in reader:
            try:
                activated_date = parse_date(row.get('activated'))
                deactivated_date = parse_date(row.get('deactivated'))

                device = Device(
                    device_manage_id=row['device_manage_id'],
                    acct_num=row['acct_num'],
                    profile_id=row['profile_id'],
                    serial_number=row['serial_number'],
                    activated=activated_date,
                    deactivated=deactivated_date,
                    ppid=row['ppid'],
                    modal_name=row.get('modal_name', ''),
                    internet_mail_id=row.get('internet_mail_id', ''),
                    alias=row.get('alias', ''),
                    remarks=row.get('remarks', '')
                )
                devices_to_create.append(device)

            except ValidationError as e:
                errors.append(f"Row {row}: {e}")

        # Bulk create devices
        if devices_to_create:
            Device.objects.bulk_create(devices_to_create)

        # Sync with DeviceRecent
        for device in devices_to_create:
            DeviceRecent.objects.update_or_create(
                device_manage_id=device.device_manage_id,
                activated=device.activated,
                defaults={
                    'acct_num': device.acct_num,
                    'profile_id': device.profile_id,
                    'serial_number': device.serial_number,
                    'deactivated': device.deactivated,
                    'ppid': device.ppid,
                }
            )

        # 메시지 출력
        if errors:
            for error in errors:
                messages.error(request, error)
        else:
            messages.success(request, 'CSV 파일이 성공적으로 업로드되었습니다.')

        return redirect('device:device_list')


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

# class DeviceViewSet(viewsets.ModelViewSet):
#     queryset = Device.objects.all()
#     serializer_class = DeviceSerializer
#     filter_backends = [filters.OrderingFilter, filters.SearchFilter]
#     pagination_class = PageNumberPagination
class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    pagination_class = PageNumberPagination
    search_fields = ['device_manage_id', 'serial_number']
    ordering_fields = ['activated', 'deactivated']

# class DeviceRecentViewSet(ReadOnlyModelViewSet):
#     queryset = DeviceRecent.objects.all()
#     serializer_class = DeviceRecentSerializer
class DeviceRecentViewSet(ReadOnlyModelViewSet):
    queryset = DeviceRecent.objects.all()
    serializer_class = DeviceRecentSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    pagination_class = PageNumberPagination
    search_fields = ['device_manage_id', 'serial_number']
    ordering_fields = ['activated', 'deactivated']

def SyncDeviceToRecent(request):
    synced_count = sync_device_to_recent()
    messages.success(request, f'{synced_count} records successfully synced to device_recent.')
    return redirect('device:device_list')