### CSV 파일 처리 및 cdr 테이블에 데이터를 삽입하는 뷰 정의

import csv
import io
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CDR
from .models import DataRecord
from .forms import CSVUploadForm

def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            decoded_file = csv_file.read().decode('utf-8')
            io_string = io.StringIO(decoded_file)
            next(io_string)
            for row in csv.reader(io_string, delimiter=','):
                CDR.objects.create(
                    RECORD_TYPE=row[0],
                    RECORD_ID=row[1],
                    DATESTAMP=row[2],
                    TRANSACTION_TYPE=row[3],
                    DISCOUNT_CODE=row[4],
                    D_PRODUCT=row[5],
                    MSG_ID=row[6],
                    VOLUME_UNIT_TYPE=row[7],
                    VOLUME_UNITS=row[8],
                    ACCESS_ID=row[9],
                    PROFILE_ID=row[10],
                    MOBILE_ID=row[11],
                    REGION=row[12],
                    AMOUNT=row[13],
                    FIELD_TYPE=row[14]
                )
            return HttpResponse("CSV 파일이 성공적으로 업로드 되었습니다.")
    else:
        form = CSVUploadForm()
    return render(request, 'upload.html', {'form': form})
