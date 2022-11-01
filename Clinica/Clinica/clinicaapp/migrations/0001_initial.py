# Generated by Django 4.1.2 on 2022-11-01 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Doctores",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=20)),
                ("apellido", models.CharField(max_length=20)),
                ("dni", models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name="Turnos",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("doctor", models.CharField(max_length=20)),
                ("paciente", models.CharField(max_length=20)),
            ],
        ),
    ]
