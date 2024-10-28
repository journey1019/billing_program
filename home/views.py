from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Cdr, NetworkReport
from .forms import CDRUploadForm, NetworkReportUploadForm
import csv
import io

# CDR CSV 파일 업로드
# def upload_file(request):
#     if request.method == 'POST':
#         form = CDRUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             csv_file = request.FILES['csv_file']
#             # CSV 파일 읽기
#             if csv_file.name.endswith('.csv'):
#                 # 인코딩 처리
#                 decoded_file = io.TextIOWrapper(csv_file.file, encoding='utf-8')
#                 reader = csv.reader(decoded_file)
#                 next(reader)  # CSV 헤더 건너뛰기
#                 for row in reader:
#                     Cdr.objects.create(
#                         record_type=row[0],
#                         record_id=int(row[1]),
#                         datestamp=row[2],
#                         transaction_type=row[3],
#                         discount_code=row[4],
#                         d_product=row[5],
#                         msg_id=int(row[6]),
#                         volume_unit_type=row[7],
#                         volume_units=int(row[8]),
#                         access_id=row[9],
#                         profile_id=int(row[10]),
#                         mobile_id=row[11],
#                         region=row[12],
#                         amount=int(row[13]),
#                     )
#                 return redirect('home')  # 데이터 업로드 후 홈으로 리다이렉트
#     else:
#         form = CDRUploadForm()
#     return render(request, 'home/upload.html', {'form': form})
def upload_file(request):
    if request.method == 'POST':
        form = CDRUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            if csv_file.name.endswith('.csv'):
                decoded_file = csv_file.read().decode('utf-8')
                io_string = io.StringIO(decoded_file)
                next(io_string)  # Skip the header row
                for row in csv.reader(io_string, delimiter=','):
                    _, created = Cdr.objects.update_or_create(
                        record_type=row[0],
                        record_id=row[1],
                        datestamp=row[2],
                        transaction_type=row[3],
                        discount_code=row[4],
                        d_product=row[5],
                        msg_id=row[6],
                        volume_unit_type=row[7],
                        volume_units=row[8],
                        access_id=row[9],
                        profile_id=row[10],
                        mobile_id=row[11],
                        region=row[12],
                        amount=row[13]
                    )
                return redirect('home')
    else:
        form = CDRUploadForm()
    return render(request, 'upload.html', {'form': form})

# Network Report CSV 파일 업로드
def upload_network_report(request):
    if request.method == 'POST':
        form = NetworkReportUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            if csv_file.name.endswith('.csv'):
                decoded_file = csv_file.read().decode('utf-8')
                io_string = io.StringIO(decoded_file)
                next(io_string)  # Skip the header row
                for row in csv.reader(io_string, delimiter=','):
                    _, created = NetworkReport.objects.update_or_create(
                        sp_id=row[0],
                        serial_number=row[1],
                        terminal_id=row[2],
                        activated=row[3],
                        sid=row[4],
                        psn=row[5],
                        mode=row[6],
                        feature_options=row[7],
                        profile_id=row[8],
                        profile_name=row[9],
                        profiles=row[10],
                        ip_service_address=row[11],
                    )
                return redirect('home')
    else:
        form = NetworkReportUploadForm()
    return render(request, 'home/upload_network_report.html', {'form': form})

# 홈 화면
def home(request):
    cdrs = Cdr.objects.all()  # 모든 CDR 데이터 가져오기
    network_reports = NetworkReport.objects.all()
    return render(request, 'home/home.html', {'cdrs': cdrs, 'network_reports': network_reports})