# Generated by Django 4.0.5 on 2023-07-01 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0002_alter_vehiculomodel_categoria_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehiculomodel',
            old_name='serial_carroceroa',
            new_name='serial_carroceria',
        ),
    ]
