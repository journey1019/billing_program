# Generated by Django 5.1.2 on 2024-11-27 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('acct_num', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('acct_name', models.CharField(max_length=64)),
                ('acct_residentnum', models.BigIntegerField()),
                ('classification', models.CharField(max_length=64)),
                ('invoice_address', models.CharField(max_length=100)),
                ('invoice_address_2', models.CharField(max_length=100)),
                ('invoice_postcode', models.BigIntegerField()),
            ],
            options={
                'db_table': 'account',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cdr',
            fields=[
                ('record_type', models.CharField(max_length=3)),
                ('record_id', models.IntegerField()),
                ('datestamp', models.DateTimeField()),
                ('transaction_type', models.CharField(max_length=3)),
                ('discount_code', models.CharField(max_length=5)),
                ('d_product', models.CharField(max_length=10)),
                ('msg_id', models.BigIntegerField()),
                ('volume_unit_type', models.CharField(max_length=3)),
                ('volume_units', models.IntegerField()),
                ('access_id', models.CharField(max_length=100, null=True)),
                ('profile_id', models.IntegerField()),
                ('serial_number', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('region', models.CharField(max_length=10, null=True)),
                ('amount', models.IntegerField()),
                ('date', models.DateField(default='2000-01-01')),
                ('date_index', models.CharField(default='2000-01', max_length=10)),
            ],
            options={
                'db_table': 'cdr',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DeviceManage',
            fields=[
                ('device_manage_id', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('acct_num', models.CharField(max_length=100)),
                ('profile_id', models.IntegerField()),
                ('serial_number', models.CharField(max_length=64)),
                ('activated', models.DateField()),
                ('deactivated', models.DateField()),
                ('ppid', models.IntegerField()),
                ('modal_name', models.CharField(max_length=64)),
                ('internet_mail_id', models.CharField(max_length=100)),
                ('alias', models.CharField(blank=True, max_length=100, null=True)),
                ('remarks', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'device',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NetworkReport',
            fields=[
                ('sp_id', models.IntegerField()),
                ('serial_number', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('terminal_id', models.CharField(max_length=64, null=True)),
                ('activated', models.DateTimeField(blank=True, null=True)),
                ('sid', models.CharField(max_length=64, null=True)),
                ('psn', models.CharField(max_length=64, null=True)),
                ('mode', models.CharField(max_length=64)),
                ('feature_options', models.CharField(max_length=64)),
                ('profile_id', models.IntegerField()),
                ('profile_name', models.CharField(max_length=64)),
                ('profiles', models.IntegerField()),
                ('ip_service_address', models.CharField(max_length=100, null=True)),
            ],
            options={
                'db_table': 'nr',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PricePlan',
            fields=[
                ('ppid', models.IntegerField(primary_key=True, serialize=False)),
                ('basic_fee', models.IntegerField()),
                ('subscription_fee', models.IntegerField()),
                ('free_byte', models.IntegerField()),
                ('surcharge_unit', models.IntegerField()),
                ('each_surcharge_fee', models.FloatField()),
                ('apply_company', models.CharField(max_length=64)),
                ('remarks', models.CharField(max_length=100)),
                ('note', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'pplan',
                'managed': False,
            },
        ),
    ]
