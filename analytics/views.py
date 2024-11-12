# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from cdr.models import CDR
from .serializers import CdrDeviceDataSerializer

class CdrDeviceView(APIView):
    def get(self, request, *args, **kwargs):
        # 모든 Cdr 객체 가져오기
        cdr_data = CDR.objects.all()

        # 시리얼라이저로 데이터 직렬화 및 가공
        serializer = CdrDeviceDataSerializer(cdr_data, many=True)

        # 객체의 개수를 구함
        count = cdr_data.count()

        # 가공된 JSON 데이터를 반환
        return Response({
            "count": count,
            "results": serializer.data,
            "status":status.HTTP_200_OK
        })
