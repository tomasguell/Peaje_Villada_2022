# Generated by Django 4.1.2 on 2022-11-11 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "AppPeaje",
            "0012_remove_turnos_fechahorafin_alter_tipodocumento_tipo_and_more",
        )
    ]

    operations = [
        migrations.RemoveField(model_name="turnos", name="HoraComienzo"),
        migrations.AlterField(
            model_name="tipodocumento",
            name="tipo",
            field=models.CharField(
                choices=[
                    ("Documento de identidad", "DNI"),
                    ("Pasaporte nacional", "Pasaporte"),
                    ("Internacional", "CIF"),
                ],
                default="DNI",
                max_length=30,
            ),
        ),
        migrations.AlterField(
            model_name="tipovehiculo",
            name="tipo",
            field=models.CharField(
                choices=[
                    ("5/6 ejes", "Camion 5 ejes"),
                    ("1 eje", "Motocicleta"),
                    ("3 ejes", "Camion"),
                    ("2 ejes", "Auto"),
                    ("mas 6 ejes", "Camion mas 6 ejes"),
                    ("3/4 ejes", "Auto con carro"),
                ],
                default="",
                max_length=30,
            ),
        ),
        migrations.AlterField(
            model_name="turnos",
            name="HoraPlanificadacomienzo",
            field=models.CharField(
                choices=[
                    ("dia", "08:00 - 16:00"),
                    ("madrugada", "00:00 - 08:00 "),
                    ("noche", "16:00 - 00:00"),
                ],
                default="00:00 - 08:00",
                max_length=14,
            ),
        ),
        migrations.AlterField(
            model_name="turnos",
            name="sentidoCirculacion",
            field=models.CharField(
                choices=[
                    ("N-S", "norte-sur"),
                    ("E-O", "este-oeste"),
                    ("O-E)", "oeste-este"),
                    ("S-N", "sur-norte"),
                ],
                default="este-oeste",
                max_length=10,
            ),
        ),
    ]