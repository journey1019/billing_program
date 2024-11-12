# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from cdr.models import CDR
from .serializers import CdrDeviceDataSerializer

class CdrDeviceView(APIView):
    def get(self, request, *args, **kwargs):
        # 필수 파라미터인 date_index를 가져옴
        date_index = request.query_params.get('date_index')
        # 선택 파라미터인 serial_number을 가져옴
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

        # 직렬화
        serializer = CdrDeviceDataSerializer(queryset, many=True)

        # 필터링된 객체 수를 계산하여 응답에 포함
        count = queryset.count()

        return Response({
            "count": count,
            "results": serializer.data,
        })

