# Generated by Django 4.0.5 on 2023-07-12 23:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0004_alter_vehiculomodel_categoria_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehiculomodel',
            options={'permissions': (('visualizar_catalogo', 'Puede visualizar_catalogo'), ('adds_vehiculomodel', 'Puede adds_vehiculomodel'))},
        ),
    ]
