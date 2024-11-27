from math import ceil
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, timedelta
from calendar import monthrange
from cdr.models import CDR
from device.models import Device
from account.models import Account
from pplan.models import Pplan
from .serializers import CdrDeviceDataSerializer

class CdrDeviceView(APIView):
    def get(self, request, *args, **kwargs):
        # 필수 파라미터인 date_index를 가져옴
        date_index = request.query_params.get('date_index')
        serial_number = request.query_params.get('serial_number')

        if not date_index:
            return Response(
                {"error": "date_index parameter is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # 기본 쿼리셋: date_index를 기준으로 필터링
        queryset = CDR.objects.filter(date_index=date_index)

        # serial_number 파라미터가 제공되면 해당 조건 추가 필터링
        if serial_number:
            queryset = queryset.filter(serial_number=serial_number)

        # date_stamp 기준으로 정렬
        queryset = queryset.order_by('date_stamp')

        # `results` 배열 가져오기
        results = CdrDeviceDataSerializer(queryset, many=True).data

        # `d_product`가 `%DCT`로 끝나는 값이 있는지 확인
        dct_indices = [i for i, record in enumerate(queryset) if record.d_product.endswith('DCT')]

        # `total_day` 계산을 위한 로직
        total_day = 0
        if dct_indices:
            previous_date = None

            # `%DCT` 기준으로 데이터 분리하여 일수 계산
            for i, index in enumerate(dct_indices):
                start_date = queryset[0 if i == 0 else dct_indices[i-1] + 1].date_only
                end_date = queryset[index].date_only

                # start_date와 end_date가 datetime 객체로 저장되므로 직접 계산
                total_day += (end_date - start_date).days

            # `%DCT` 이후 추가 데이터가 있으면 그 이후 일수도 계산
            if dct_indices[-1] + 1 < len(queryset):
                start_date = queryset[dct_indices[-1] + 1].date_only
                end_date = queryset.last().date_only
                total_day += (end_date - start_date).days
        else:
            # `d_product`가 `%DCT`로 끝나는 게 없을 경우
            start_date = queryset[0].date_only
            last_day_of_month = monthrange(start_date.year, start_date.month)[1]
            end_date = start_date.replace(day=last_day_of_month)
            total_day = (end_date - start_date).days + 1

        # `month_day` 계산 (월의 총 일수)
        first_record = queryset.first()
        if first_record:
            year, month = first_record.date_only.year, first_record.date_only.month
            month_day = monthrange(year, month)[1]
        else:
            month_day = 0

        # 데이터와 관련된 추가 필드 계산
        serial_number = queryset.first().serial_number if queryset.exists() else None
        device = Device.objects.filter(serial_number=serial_number).first() if serial_number else None
        account = Account.objects.filter(acct_num=device.acct_num).first() if device else None
        pplan = Pplan.objects.filter(ppid=device.ppid).first() if device else None

        # Pplan 에서 `free_byte` 값을 가져옴
        free_byte = pplan.free_byte if pplan else 0

        # `bill` 계산 (total_day / month_day, 소수점 둘째 자리까지 올림)
        bill = ceil(total_day / month_day * 100) / 100 if month_day else 0

        # `total_used_bytes` 계산 (d_product='%DAT'인 경우 volume_units 모두 더함)
        total_used_bytes = sum(record.volume_units for record in queryset if record.d_product.endswith('DAT'))

        # `add_used_bytes` 계산 (total_used_bytes > free_byte ? total_used_bytes - free_byte : 0)
        add_used_bytes = total_used_bytes - free_byte if total_used_bytes > free_byte else 0

        # `total_subscription_fee` 계산 (d_product='%ACT'일 때 subscription_fee)
        total_subscription_fee = sum(record.subscription_fee for record in queryset if record.d_product.endswith('ACT'))

        # `total_basic_fee` 계산 (d_product='%MMF'일 때 basic_fee * bill)
        #total_basic_fee = sum(record.basic_fee * bill for record in queryset if record.d_product.endswith('MMF'))
        total_basic_fee = next(
            (record['basic_fee'] * bill for record in results if record['d_product'].endswith('MMF')),
            0  # 조건에 맞는 객체가 없으면 0으로 설정
        )

        # `add_used_fee` 계산 (add_used_bytes / (surcharge_unit * each_surcharge_fee * bill))
        surcharge_unit = pplan.surcharge_unit if pplan else 1  # 기본값 1, 실제로는 pplan에서 가져올 값 사용
        each_surcharge_fee = pplan.each_surcharge_fee if pplan else 0  # 기본값 1, 실제로는 pplan에서 가져올 값 사용
        # add_used_fee = add_used_bytes / (surcharge_unit * each_surcharge_fee * bill) if add_used_bytes > 0 else 0
        if surcharge_unit * each_surcharge_fee * bill != 0:
            add_used_fee = add_used_bytes / surcharge_unit * each_surcharge_fee * bill if add_used_bytes > 0 else 0
        else:
            add_used_fee = 0  # 나누는 값이 0인 경우, add_used_fee는 0으로 설정

        # `total_month_fee` 계산
        total_month_fee = total_subscription_fee + total_basic_fee + add_used_fee

        response_data = {
            "count": queryset.count(),
            "serial_number": serial_number,
            "acct_num": device.acct_num if device else None,
            "acct_name": account.acct_name if account else None,
            "ppid": device.ppid if device else None,
            "basic_fee": pplan.basic_fee if pplan else None,
            "subscription_fee": pplan.subscription_fee if pplan else None,
            "free_byte": pplan.free_byte if pplan else None,
            "surcharge_unit": pplan.surcharge_unit if pplan else None,
            "each_surcharge_fee": pplan.each_surcharge_fee if pplan else None,
            "apply_company": pplan.apply_company if pplan else None,
            "remarks": pplan.remarks if pplan else None,
            "note": pplan.note if pplan else None,
            "month_day": month_day,
            "total_day": total_day,
            "bill": bill,
            "total_used_bytes": total_used_bytes,
            "add_used_bytes": add_used_bytes,
            "total_subscription_fee": round(total_subscription_fee),
            "total_basic_fee": round(total_basic_fee),
            "add_used_fee": round(add_used_fee),
            "total_month_fee": round(total_month_fee),
            "results": CdrDeviceDataSerializer(queryset, many=True).data
        }
        if not serial_number:
            response_data = {
                "count": response_data["count"],
                "results": CdrDeviceDataSerializer["results"]
            }


        return Response(response_data)

# http://127.0.0.1:8000/analytics/api/cdr-device/?date_index=202409&serial_number=01820340SKY9FC1
# http://127.0.0.1:8000/analytics/api/cdr-device/?date_index=202409&serial_number=01680386SKY2A47