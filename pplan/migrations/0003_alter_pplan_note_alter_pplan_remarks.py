# Generated by Django 5.1.2 on 2024-11-15 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pplan', '0002_alter_pplan_note_alter_pplan_remarks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pplan',
            name='note',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pplan',
            name='remarks',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
