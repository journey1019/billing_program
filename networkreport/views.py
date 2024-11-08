import csv
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.dateparse import parse_datetime

from .models import NetworkReport, UploadedNRFile
from django.db import IntegrityError
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from .serializers import NetworkReportSerializer


def NetworkReportUploadCSV(request):
    if request.method == "POST":
        csv_files = request.FILES.getlist("csv_file")
        for csv_file in csv_files:
            if UploadedNRFile.objects.filter(file_name=csv_file.name).exists():
                messages.error(request, f"파일 '{csv_file.name}'은 이미 업로드된 파일입니다.")
                continue

            file_data = csv_file.read().decode("utf-8").splitlines()
            csv_reader = csv.DictReader(file_data)
            transformed_data = [
                {k.lower(): v for k, v in row.items()} for row in csv_reader  # 컬럼명을 소문자로 변환
            ]

            for row in transformed_data:
                row["ip_service_address"] = row.pop("IP_SERVICE_ADDRESS", None)

                # activated 필드가 없거나 NULL일 경우 기본 날짜로 설정
                activated_value = row.get("activated")
                if not activated_value or activated_value.upper() == "NULL":
                    activated_value = "2000-01-01 00:00:00.000"

                # Parse the activated value into a datetime object
                activated_dt = parse_datetime(activated_value)

                existing_nr = NetworkReport.objects.filter(
                    sp_id=row["sp_id"],
                    serial_number=row["serial_number"],
                    activated=activated_dt
                ).first()

                if existing_nr:
                    print(f"중복된 값 발견: sp_id={row['sp_id']}, serial_number={row['serial_number']}, activated={row['activated']}")
                else:
                    try:
                        NetworkReport.objects.update_or_create(
                            sp_id=row["sp_id"],
                            serial_number=row["serial_number"],
                            activated=activated_dt,
                            defaults={
                                "terminal_id": row.get("terminal_id"),
                                "sid": row.get("sid"),
                                "psn": row.get("psn"),
                                "mode": row.get("mode"),
                                "feature_options": row.get("feature_options"),
                                "profile_id": row.get("profile_id"),
                                "profile_name": row.get("profile_name"),
                                "profiles": row.get("profiles"),
                                "ip_service_address": row.get("ip_service_address"),
                            }
                        )
                    except IntegrityError:
                        print(f"중복된 값 발견 (예외 처리): sp_id={row['sp_id']}, serial_number={row['serial_number']}, activated={row['activated']}")

            uploaded_file = UploadedNRFile(file_name=csv_file.name, file=csv_file)
            uploaded_file.save()

            messages.success(request, f"파일 '{csv_file.name}' 이 성공적으로 업로드되었습니다.")
        return redirect("nr:upload_nr")

    uploaded_nr_files = UploadedNRFile.objects.all()
    nr_data = NetworkReport.objects.all()
    return render(request, "nr/upload_nr.html", {"uploaded_nr_files": uploaded_nr_files, "nr_data": nr_data})

def NRTable(request):
    nr_data = NetworkReport.objects.all()
    paginator = Paginator(nr_data, 50)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "nr/nr_table.html", {"page_obj": page_obj})

class NRViewSet(viewsets.ModelViewSet): # ModelViewSet은
    queryset = NetworkReport.objects.all()  # 모든 NR 객체를 반환
    serializer_class = NetworkReportSerializer  # 직렬화 클래스 설정
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]

    # 페이지네이션 설정
    pagination_class = PageNumberPagination