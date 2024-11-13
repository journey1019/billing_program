from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, timedelta
from calendar import monthrange
from cdr.models import CDR
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

        # datestamp 기준으로 정렬
        queryset = queryset.order_by('datestamp')

        # `d_product`가 `%DCT`로 끝나는 값이 있는지 확인
        dct_indices = [i for i, record in enumerate(queryset) if record.d_product.endswith('DCT')]

        # `total_day` 계산을 위한 로직
        total_day = 0
        if dct_indices:
            previous_date = None

            # `%DCT` 기준으로 데이터 분리하여 일수 계산
            for i, index in enumerate(dct_indices):
                start_date = queryset[0 if i == 0 else dct_indices[i-1] + 1].date
                end_date = queryset[index].date
                start_date = datetime.strptime(start_date, "%Y-%m-%d") if isinstance(start_date, str) else start_date
                end_date = datetime.strptime(end_date, "%Y-%m-%d") if isinstance(end_date, str) else end_date
                total_day += (end_date - start_date).days

            # `%DCT` 이후 추가 데이터가 있으면 그 이후 일수도 계산
            if dct_indices[-1] + 1 < len(queryset):
                start_date = queryset[dct_indices[-1] + 1].date
                end_date = queryset.last().date
                start_date = datetime.strptime(start_date, "%Y-%m-%d") if isinstance(start_date, str) else start_date
                end_date = datetime.strptime(end_date, "%Y-%m-%d") if isinstance(end_date, str) else end_date
                total_day += (end_date - start_date).days
        else:
            # `d_product`가 `%DCT`로 끝나는 게 없을 경우
            start_date = queryset[0].date
            start_date = datetime.strptime(start_date, "%Y-%m-%d") if isinstance(start_date, str) else start_date
            last_day_of_month = monthrange(start_date.year, start_date.month)[1]
            end_date = start_date.replace(day=last_day_of_month)
            total_day = (end_date - start_date).days + 1

        # 직렬화
        serializer = CdrDeviceDataSerializer(queryset, many=True)

        return Response({
            "count": queryset.count(),
            "total_day": total_day,
            "results": serializer.data,
        })
