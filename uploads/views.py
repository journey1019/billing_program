import csv
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CDR
from .forms import CSVUploadForm
from django.db.utils import IntegrityError

def upload_csv(request):
    if request.method == "POST":
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES["file"]
            if not csv_file.name.endswith(".csv"):
                messages.error(request, "CSV 파일만 업로드할 수 있습니다.")
                return redirect("upload_csv")

            decoded_file = csv_file.read().decode("utf-8").splitlines()
            reader = csv.DictReader(decoded_file)

            cdr_entries = []
            for row in reader:
                try:
                    cdr_entry = CDR(
                        record_type=row["record_type"],
                        record_id=row["record_id"],
                        datestamp=row["datestamp"],
                        transaction_type=row["transaction_type"],
                        discount_code=row["discount_code"],
                        d_product=row["d_product"],
                        msg_id=row["msg_id"],
                        volume_unit_type=row["volume_unit_type"],
                        volume_units=row["volume_units"],
                        access_id=row.get("access_id", None),
                        profile_id=row["profile_id"],
                        serial_number=row["serial_number"],
                        region=row.get("region", None),
                        amount=row["amount"],
                    )
                    cdr_entries.append(cdr_entry)
                except KeyError as e:
                    messages.error(request, f"잘못된 컬럼명: {e}")
                    return redirect("upload_csv")

            try:
                CDR.objects.bulk_create(cdr_entries, ignore_conflicts=True) # 중복 항목을 무시하고 새 레코드만 삽입
                messages.success(request, "CSV 데이터를 성공적으로 업로드하였습니다.")
            except IntegrityError:
                messages.error(request, "중복 데이터가 포함되어 일부 항목이 생략되었습니다.")

            return redirect("upload_csv")
    else:
        form = CSVUploadForm()

    return render(request, "uploads/upload_csv.html", {"form": form})
