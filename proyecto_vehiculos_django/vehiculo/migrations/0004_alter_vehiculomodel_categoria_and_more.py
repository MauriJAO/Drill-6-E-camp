# Generated by Django 4.0.5 on 2023-07-01 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0003_rename_serial_carroceroa_vehiculomodel_serial_carroceria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculomodel',
            name='categoria',
            field=models.CharField(choices=[('Particular', 'Particular'), ('Transporte', 'Transporte'), ('Carga', 'Carga')], max_length=20),
        ),
        migrations.AlterField(
            model_name='vehiculomodel',
            name='marca',
            field=models.CharField(choices=[('Ford', 'Ford'), ('Chevrolet', 'Chevrolet'), ('Fiat', 'Fiat'), ('Toyota', 'Toyota')], max_length=20),
        ),
    ]
