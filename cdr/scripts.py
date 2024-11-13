from cdr.models import CDR, CDRSummary
from datetime import datetime

def migrate_dates():
    for cdr in CDR.objects.all():
        try:
            cdr.datestamp = datetime.strptime(cdr.datestamp, "%Y-%m-%d %H:%M:%S")
            cdr.date = cdr.datestamp.date()
            cdr.date_index = cdr.datestamp.strftime("%Y%m")
            cdr.save()
        except ValueError:
            print(f"Error parsing datestamp for CDR id={cdr.id}")

    for summary in CDRSummary.objects.all():
        try:
            summary.datestamp = datetime.strptime(summary.datestamp, "%Y-%m-%d %H:%M:%S")
            summary.date = summary.datestamp.date()
            summary.date_index = summary.datestamp.strftime("%Y%m")
            summary.save()
        except ValueError:
            print(f"Error parsing datestamp for CDRSummary id={summary.id}")

# 호출
migrate_dates()
