# Generated by Django 5.1.2 on 2024-11-27 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceRecent',
            fields=[
                ('device_manage_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('acct_num', models.CharField(max_length=10)),
                ('profile_id', models.IntegerField()),
                ('serial_number', models.CharField(max_length=64)),
                ('activated', models.DateField()),
                ('deactivated', models.DateField(blank=True, null=True)),
                ('ppid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('device_manage_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('acct_num', models.CharField(max_length=10)),
                ('profile_id', models.IntegerField()),
                ('serial_number', models.CharField(max_length=64)),
                ('activated', models.DateField()),
                ('deactivated', models.DateField(blank=True, null=True)),
                ('ppid', models.IntegerField()),
                ('modal_name', models.CharField(blank=True, max_length=64, null=True)),
                ('internet_mail_id', models.CharField(blank=True, max_length=100, null=True)),
                ('alias', models.CharField(blank=True, max_length=100, null=True)),
                ('remarks', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'unique_together': {('device_manage_id', 'activated')},
            },
        ),
    ]
