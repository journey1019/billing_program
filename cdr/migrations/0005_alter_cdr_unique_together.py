# Generated by Django 5.1.2 on 2024-11-14 02:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cdr', '0004_rename_date_cdr_date_only_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cdr',
            unique_together={('record_id', 'serial_number', 'date_stamp', 'd_product', 'msg_id')},
        ),
    ]
