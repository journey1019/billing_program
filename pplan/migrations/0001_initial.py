# Generated by Django 5.1.2 on 2024-11-11 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pplan',
            fields=[
                ('ppid', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('basic_fee', models.IntegerField()),
                ('subscription_fee', models.IntegerField()),
                ('free_byte', models.IntegerField()),
                ('surcharge_unit', models.IntegerField()),
                ('each_surcharge_fee', models.FloatField()),
                ('apply_company', models.CharField(max_length=64)),
                ('remarks', models.CharField(max_length=100)),
                ('note', models.CharField(max_length=100)),
            ],
        ),
    ]