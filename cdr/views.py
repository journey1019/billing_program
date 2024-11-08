import csv
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CDR, UploadedFile
from datetime import datetime
from django.db import IntegrityError
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from .serializers import CDRSerializer

# CDR.csv Upload
def CDRUploadCSV(request):
    if request.method == "POST":
        csv_files = request.FILES.getlist("csv_file")  # 여러 파일을 가져옴
        for csv_file in csv_files:
            # 중복된 파일 이름을 체크
            if UploadedFile.objects.filter(file_name=csv_file.name).exists():
                messages.error(request, f"파일 '{csv_file.name}'은 이미 업로드된 파일입니다.")
                continue  # 중복된 파일은 건너뜀

            # CSV 파일을 텍스트로 읽고, 컬럼명을 소문자로 변환
            file_data = csv_file.read().decode("utf-8").splitlines()
            csv_reader = csv.DictReader(file_data)
            transformed_data = [
                {k.lower(): v for k, v in row.items()} for row in csv_reader  # 컬럼명을 소문자로 변환
            ]

            # mobile_id를 serial_number로 변환하고, date와 date_index 필드도 생성
            for row in transformed_data:
                row["serial_number"] = row.pop("mobile_id", None)  # mobile_id -> serial_number

                # datestamp를 그대로 문자열로 사용 (형식: "2024-08-01 00:00:00")
                datestamp = row["datestamp"]
                date = datestamp.split()[0]  # "YYYY-MM-DD"
                date_index = datestamp.replace("-", "")[:6]  # "YYYYMM"

                # 중복 여부 체크 (unique_together 필드를 기준으로)
                existing_cdr = CDR.objects.filter(
                    serial_number=row["serial_number"],
                    datestamp=datestamp,
                    d_product=row["d_product"],
                    msg_id=row["msg_id"]
                ).first()

                if existing_cdr:
                    # 중복된 값이 있으면 터미널에 출력
                    print(f"중복된 값 발견: serial_number={row['serial_number']}, msg_id={row['msg_id']}, datestamp={datestamp}, d_product={row['d_product']}")
                else:
                    # 중복된 값이 없다면 데이터를 저장
                    try:
                        CDR.objects.update_or_create(
                            serial_number=row["serial_number"],
                            msg_id=row["msg_id"],
                            d_product=row["d_product"],
                            datestamp=datestamp,  # 문자열 그대로 저장
                            defaults={
                                "record_type": row.get("record_type"),
                                "record_id": row.get("record_id"),
                                "transaction_type": row.get("transaction_type"),
                                "discount_code": row.get("discount_code"),
                                "volume_unit_type": row.get("volume_unit_type"),
                                "volume_units": row.get("volume_units"),
                                "access_id": row.get("access_id"),
                                "profile_id": row.get("profile_id"),
                                "region": row.get("region"),
                                "amount": row.get("amount"),
                                "date": date,  # YYYY-MM-DD 형식으로 저장
                                "date_index": date_index  # YYYYMM 형식으로 저장
                            }
                        )
                    except IntegrityError:
                        # 중복된 값 발견 시 예외 처리
                        print(f"중복된 값 발견 (예외 처리): serial_number={row['serial_number']}, msg_id={row['msg_id']}, datestamp={datestamp}, d_product={row['d_product']}")

            # 업로드된 파일을 기록
            uploaded_file = UploadedFile(file_name=csv_file.name, file=csv_file)
            uploaded_file.save()

            messages.success(request, f"파일 '{csv_file.name}' 이 성공적으로 업로드되었습니다.")
        return redirect("cdr:upload_csv")

    # 업로드된 파일 목록 조회
    uploaded_files = UploadedFile.objects.all()
    cdr_data = CDR.objects.all()
    return render(request, "cdr/upload_csv.html", {"uploaded_files": uploaded_files, "cdr_data": cdr_data})

# CDR Table
def CDRTable(request):
    cdr_data = CDR.objects.all()
    paginator = Paginator(cdr_data, 50)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "cdr/cdr_table.html", {"page_obj": page_obj})

# CDR API
class CDRViewSet(viewsets.ModelViewSet): # ModelViewSet은
    queryset = CDR.objects.all()  # 모든 CDR 객체를 반환
    serializer_class = CDRSerializer  # 직렬화 클래스 설정
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['record_type', 'region']  # 검색할 필드
    ordering_fields = ['datestamp']  # 정렬할 필드
    ordering = ['-datestamp']  # 기본 정렬 기준

    # 페이지네이션 설정
    pagination_class = PageNumberPagination