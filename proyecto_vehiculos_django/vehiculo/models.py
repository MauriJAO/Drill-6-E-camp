from django.db import models

# Create your models here.

class VehiculoModel(models.Model):

    MARCA_CHOICES = [
        ('Ford', 'Ford'),
        ('Chevrolet', 'Chevrolet'),
        ('Fiat', 'Fiat'),
        ('Toyota', 'Toyota'),
    ]

    CATEGORIA_CHOICES = [
        ('Particular', 'Particular'),
        ('Transporte', 'Transporte'),
        ('Carga', 'Carga')
    ]

    marca = models.CharField(max_length=20, choices=MARCA_CHOICES)
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES)
    precio = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        permissions = (
            ("visualizar_catalogo", "Puede visualizar_catalogo"),
            ("adds_vehiculomodel", "Puede adds_vehiculomodel")
        )


    def __str__(self):
        return self.marca
