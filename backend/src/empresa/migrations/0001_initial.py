# Generated by Django 4.2.4 on 2023-08-06 20:40

from django.db import migrations, models
import lib.validator


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Empresa",
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
                (
                    "CNPJ",
                    models.CharField(
                        max_length=18,
                        unique=True,
                        validators=[lib.validator.CnpjValidator()],
                    ),
                ),
                ("razao_social", models.CharField(max_length=500)),
                ("nome_fantasia", models.CharField(max_length=500)),
                ("CNAE_principal", models.CharField(max_length=1000)),
            ],
        ),
    ]