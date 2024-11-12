# billing/views.py
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db import connection
from django.http import JsonResponse
from .models import BillingDataView, Account, Pplan
from cdr.models import CDR
from device.models import Device
from pplan.models import Pplan
from account.models import Account
from cdr.serializers import CDRSerializer
from device.serializers import DeviceSerializer
from pplan.serializers import PplanSerializer
from account.serializers import AccountSerializer
from django.views.decorators.csrf import csrf_exempt


class AggregatedDataAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # GET 요청에서 필수 파라미터 추출
        serial_number = request.query_params.get('serial_number')
        date_index = request.query_params.get('date_index')

        if not serial_number or not date_index:
            return Response({"error": "serial_number and date_index are required parameters."},
                            status=status.HTTP_400_BAD_REQUEST)

        # 1. CDR 데이터 필터링
        cdr_records = CDR.objects.filter(serial_number=serial_number, date_index=date_index)
        if not cdr_records.exists():
            return Response({"error": "No CDR data found for the given parameters."},
                            status=status.HTTP_404_NOT_FOUND)

        # CDR 데이터 시리얼라이즈
        cdr_data = CDRSerializer(cdr_records, many=True).data

        # 2. Device 데이터 조회
        device = Device.objects.filter(serial_number=serial_number).first()
        device_data = DeviceSerializer(device).data if device else {}

        # 3. Pplan 데이터 조회 및 요금 계산
        calculated_data = []
        for cdr in cdr_data:
            ppid = device_data.get('ppid')
            pplan = Pplan.objects.filter(ppid=ppid).first()
            if not pplan:
                continue

            # 요금 계산 (예: `volume_units` * `each_surcharge_fee`)
            volume_units = cdr.get('volume_units', 0)
            surcharge_fee = pplan.each_surcharge_fee
            calculated_amount = volume_units * surcharge_fee

            # 가공된 데이터 추가
            calculated_data.append({
                "cdr": cdr,
                "device": device_data,
                "pplan": PplanSerializer(pplan).data,
                "calculated_amount": calculated_amount
            })

        return Response(calculated_data, status=status.HTTP_200_OK)


@api_view(['GET'])
def GenerateBillingData(request):
    # URL에서 date_index 파라미터를 가져옴
    date_index = request.GET.get('date_index')

    if not date_index:
        return JsonResponse({'error': 'Missing date_index parameter'}, status=400)

    # date_index에 해당하는 데이터 조회
    data = BillingDataView.objects.filter(date_index=date_index).order_by('serial_number', 'datestamp')

    # 데이터가 없다면 에러 메시지 반환
    if not data:
        return JsonResponse({'error': 'No data found for the given date_index'}, status=404)

    # 데이터를 JSON으로 변환
    result = []
    for row in data:
        result.append({
            'datestamp': row.datestamp,
            'discount_code': row.discount_code,
            'd_product': row.d_product,
            'volume_units': row.volume_units,
            'profile_id': row.profile_id,
            'serial_number': row.serial_number,
            'amount': row.amount,
            'date': row.date,
            'date_index': row.date_index,
            'acct_num': row.acct_num,
            'acct_resident_num': row.acct_resident_num,
            'basic_fee': row.basic_fee,
            'subscription_fee': row.subscription_fee,
            'free_byte': row.free_byte,
            'surcharge_unit': row.surcharge_unit,
            'each_surcharge_fee': row.each_surcharge_fee,
            'apply_company': row.apply_company,
            'remarks': row.remarks,
            'note': row.note
        })

    return JsonResponse(result, safe=False)

@api_view(['GET'])
def GetBillingDataFromView(request):
    date_index = request.GET.get('date_index', None)

    if not date_index:
        return Response({"message": "date_index parameter is required"}, status=400)

    billing_data = BillingDataView.objects.filter(date_index=date_index)

    if not billing_data:
        return Response({"message": "No data found for the given date_index"}, status=404)

    # 데이터를 직렬화하여 반환
    data = [{"datestamp": item.datestamp, "discount_code": item.discount_code, "d_product": item.d_product,
             "volume_units": item.volume_units, "serial_number": item.serial_number, "amount": item.amount,
             "date": item.date, "date_index": item.date_index, "acct_num": item.acct_num, "ppid": item.ppid}
            for item in billing_data]

    return Response({"billing_data": data}, status=200)