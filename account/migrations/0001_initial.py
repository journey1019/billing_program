# Generated by Django 5.1.2 on 2024-11-08 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('acct_num', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('acct_name', models.CharField(max_length=64)),
                ('acct_resident_num', models.IntegerField(null=True)),
                ('classification', models.CharField(max_length=100)),
                ('invoice_address', models.CharField(max_length=100, null=True)),
                ('invoice_address2', models.CharField(max_length=100, null=True)),
                ('invoice_postcode', models.IntegerField(null=True)),
            ],
            options={
                'unique_together': {('acct_num',)},
            },
        ),
    ]
