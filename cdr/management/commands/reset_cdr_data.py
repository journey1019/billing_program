from django.core.management.base import BaseCommand
from cdr.models import CDR
from cdr.models import UploadedFile
import csv
import os

class Command(BaseCommand):
    help = "Delete existing CDR data and reload from CSV file"

    def handle(self, *args, **kwargs):
        # Step 1: Delete existing data
        CDR.objects.all().delete()
        UploadedFile.objects.all().delete()
        self.stdout.write(self.style.SUCCESS("Deleted all data in CDR and UploadedFile tables."))

        # Step 2: Directory containing the CSV files
        directory_path = "/Volumes/My Passport/1.Project/python/billing/cdr/csvs/"

        # Loop through all files in the directory
        for filename in os.listdir(directory_path):
            if filename.endswith(".csv"):
                file_path = os.path.join(directory_path, filename)
                with open(file_path, mode='r') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        CDR.objects.create(
                            record_type=row['record_type'],
                            record_id=row['record_id'],
                            date_stamp=row['date_stamp'],
                            transaction_type=row['transaction_type'],
                            discount_code=row['discount_code'],
                            d_product=row['d_product'],
                            msg_id=row['msg_id'],
                            volume_unit_type=row['volume_unit_type'],
                            volume_units=row['volume_units'],
                            access_id=row.get('access_id', None),
                            profile_id=row['profile_id'],
                            serial_number=row['serial_number'],
                            region=row.get('region', None),
                            amount=row['amount'],
                        )
                self.stdout.write(self.style.SUCCESS("CDR data reloaded successfully."))
        self.stdout.write(self.stle.SUCCESS("ALL CSV files processed successfully."))
