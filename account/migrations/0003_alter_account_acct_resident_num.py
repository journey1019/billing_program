# Generated by Django 5.1.2 on 2024-11-08 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_account_acct_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='acct_resident_num',
            field=models.BigIntegerField(null=True),
        ),
    ]
