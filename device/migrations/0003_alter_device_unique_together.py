# Generated by Django 5.1.2 on 2024-11-11 02:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0002_alter_device_alias_alter_device_internet_mail_id_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='device',
            unique_together={('device_manage_id', 'activated')},
        ),
    ]