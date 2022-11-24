# Generated by Django 4.1.2 on 2022-11-17 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("AppPeaje", "0013_alter_tipodocumento_tipo_alter_tipovehiculo_tipo_and_more")
    ]

    operations = [
        migrations.AlterField(
            model_name="tipodocumento",
            name="tipo",
            field=models.CharField(
                choices=[
                    ("Pasaporte nacional", "Pasaporte"),
                    ("Documento de identidad", "DNI"),
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
                    ("3 ejes", "Camion"),
                    ("mas 6 ejes", "Camion mas 6 ejes"),
                    ("1 eje", "Motocicleta"),
                    ("5/6 ejes", "Camion 5 ejes"),
                    ("3/4 ejes", "Auto con carro"),
                    ("2 ejes", "Auto"),
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
                    ("madrugada", "00:00 - 08:00 "),
                    ("noche", "16:00 - 00:00"),
                    ("dia", "08:00 - 16:00"),
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
                    ("O-E)", "oeste-este"),
                    ("N-S", "norte-sur"),
                    ("E-O", "este-oeste"),
                    ("S-N", "sur-norte"),
                ],
                default="este-oeste",
                max_length=10,
            ),
        ),
    ]