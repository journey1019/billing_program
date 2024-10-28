# Generated by Django 5.1.2 on 2024-10-28 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cdr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_type', models.CharField(max_length=3)),
                ('record_id', models.IntegerField()),
                ('datestamp', models.DateTimeField()),
                ('transaction_type', models.CharField(max_length=3)),
                ('discount_code', models.CharField(max_length=5)),
                ('d_product', models.CharField(max_length=10)),
                ('msg_id', models.BigIntegerField()),
                ('volume_unit_type', models.CharField(max_length=3)),
                ('volume_units', models.IntegerField()),
                ('access_id', models.CharField(max_length=100)),
                ('profile_id', models.IntegerField()),
                ('mobile_id', models.CharField(max_length=64)),
                ('region', models.CharField(max_length=10)),
                ('amount', models.IntegerField()),
                ('field_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='NetworkReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sp_id', models.IntegerField()),
                ('serial_number', models.CharField(max_length=64)),
                ('terminal_id', models.CharField(max_length=64)),
                ('activated', models.DateTimeField(blank=True, null=True)),
                ('sid', models.CharField(max_length=64)),
                ('psn', models.CharField(max_length=64)),
                ('mode', models.CharField(max_length=64)),
                ('feature_options', models.CharField(max_length=64)),
                ('profile_id', models.IntegerField()),
                ('profile_name', models.CharField(max_length=64)),
                ('profiles', models.IntegerField()),
                ('ip_service_address', models.CharField(max_length=100)),
                ('field_type', models.CharField(max_length=100)),
            ],
        ),
    ]
