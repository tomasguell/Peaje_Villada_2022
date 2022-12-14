# Generated by Django 4.1.2 on 2022-11-28 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("AppPeaje", "0008_alter_tipodocumento_tipo_alter_tipovehiculo_tipo_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tipodocumento",
            name="tipo",
            field=models.CharField(
                choices=[("CIF", "CIF"), ("Pasaporte", "Pasaporte"), ("DNI", "DNI")],
                default="DNI",
                max_length=30,
            ),
        ),
        migrations.AlterField(
            model_name="tipovehiculo",
            name="tipo",
            field=models.CharField(
                choices=[
                    ("3/4 ejes < 2.10m", "3/4 ejes < 2.10m"),
                    ("> 6 ejes", "> 6 ejes"),
                    ("5/6 ejes", "5/6 ejes"),
                    ("2 ejes", "2 ejes"),
                    ("3/4 ejes > 2.10m", "3/4 ejes > 2.10m"),
                    ("Motocicletas", "Motocicletas"),
                    ("Automoviles", "Automoviles"),
                ],
                default="",
                max_length=30,
            ),
        ),
        migrations.AlterField(
            model_name="turnos",
            name="HoraPlanificada",
            field=models.CharField(
                choices=[
                    ("noche", "16:00 - 00:00"),
                    ("dia", "08:00 - 16:00"),
                    ("madrugada", "00:00 - 08:00 "),
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
                    ("sur-norte", "sur-norte"),
                    ("este-oeste", "este-oeste"),
                    ("oeste-este", "oeste-este"),
                    ("norte-sur", "norte-sur"),
                ],
                default="este-oeste",
                max_length=10,
            ),
        ),
    ]
