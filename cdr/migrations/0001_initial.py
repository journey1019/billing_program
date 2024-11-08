# Generated by Django 5.1.2 on 2024-11-08 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=225, unique=True)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(upload_to='cdr/csvs/')),
            ],
        ),
        migrations.CreateModel(
            name='CDR',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('record_type', models.CharField(max_length=3)),
                ('record_id', models.IntegerField()),
                ('datestamp', models.CharField(max_length=100)),
                ('transaction_type', models.CharField(max_length=3)),
                ('discount_code', models.CharField(max_length=5)),
                ('d_product', models.CharField(max_length=10)),
                ('msg_id', models.BigIntegerField()),
                ('volume_unit_type', models.CharField(max_length=3)),
                ('volume_units', models.IntegerField()),
                ('access_id', models.CharField(max_length=100, null=True)),
                ('profile_id', models.IntegerField()),
                ('serial_number', models.CharField(max_length=64)),
                ('region', models.CharField(max_length=10, null=True)),
                ('amount', models.IntegerField()),
                ('date', models.CharField(max_length=100)),
                ('date_index', models.CharField(max_length=100)),
            ],
            options={
                'unique_together': {('serial_number', 'datestamp', 'd_product', 'msg_id')},
            },
        ),
    ]
