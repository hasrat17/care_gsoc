# Generated by Django 4.2.6 on 2023-12-09 10:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("facility", "0402_patientconsultation_new_discharge_reason"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dailyround",
            name="rounds_type",
            field=models.IntegerField(
                choices=[
                    (0, "NORMAL"),
                    (100, "VENTILATOR"),
                    (200, "ICU"),
                    (300, "AUTOMATED"),
                    (400, "TELEMEDICINE"),
                ],
                default=0,
            ),
        ),
    ]
