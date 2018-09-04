from django.db import models

zona_option = (
    ('Torso/Espalda', '1.- TORSO/ESPALDA'),
    ('Brazo', '2.- BRAZO'),
    ('Antebrazo', '3.- ANTEBRAZO'),
    ('Muslo', '4.- MUSLO'),
    ('Pierna Baja', '5.- PIERNA BAJA'),
    ('Pie', '6.- PIE'),
    ('Cuello', '7.- CUELLO'),
    ('Manos', '8.- MANOS'),
    ('Cabeza', '9.- CABEZA'),
    ('Cadera', '10.- CADERA'))

tinta_option = (
    ('Escala grises', 'Escala de grises'),
    ('Color', 'Color'))

posicion_option = (
    ('Frente','FRENTE'),
    ('Posterior','POSTERIOR'))

anticipo_option = (
    (200,200),
    (500,500))

no_horas_option = (
    (1,'1 Hora'),
    (2,'2 Horas'),
    (3,'3 Horas'),
    (4,'4 Horas'),
    (5,'5 Horas'),
    (6,'6 Horas'),
    (7,'7 Horas'),
    (8,'8 Horas'))

tipo_pago_option = (
    ('Efectivo','Efectivo en tienda'),
    ('Transferencia','Transferenci bancaria'),
    ('Paypal','Paypal'),)


class Quotation(models.Model):
    """Cotizacion"""
    creacion = models.DateTimeField(auto_now_add=True, blank=True)
    nombre   = models.CharField(max_length=128)
    telefono = models.CharField(max_length=10)
    correo   = models.EmailField(max_length=254)
    zona     = models.CharField(max_length= 17, choices=zona_option, default='Torso/Espalda')
    tinta    = models.CharField(max_length= 16, choices=tinta_option, default='escala')
    posicion = models.CharField(max_length= 9, choices=posicion_option, default='frente')
    alto        = models.IntegerField(null=False)
    ancho       = models.IntegerField(null=False)
    referencia1 = models.ImageField(null=True, blank=True)
    referencia2 = models.ImageField(null=True, blank=True)
    referencia3 = models.ImageField(null=True, blank=True)
    descripcion = models.TextField(max_length=280, default='')
    no_horas    = models.IntegerField(default=0)
    anticipo    = models.IntegerField(default=200, choices=anticipo_option)
    precioTotal = models.IntegerField(default=0)
    comentarios = models.TextField(max_length=280, default='')
    cotizado    = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre


class Client(models.Model):
    nombre = models.CharField(max_length=128, blank=False)
    edad   = models.IntegerField(default=18)
    telefono = models.CharField(max_length=10)
    correo = models.EmailField(max_length=254)
    vicitas = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre


class Appointment(models.Model):
    cliente = models.ForeignKey(Client, on_delete=models.CASCADE)
    descripcion = models.TextField(max_length=280, default='')
    dia = models.DateField(auto_now=False, auto_now_add=False)
    start = models.TimeField(auto_now=False, auto_now_add=False)
    end = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.descripcion


class Payment(models.Model):
    cita = models.OneToOneField(Appointment, on_delete=models.CASCADE, primary_key=True)
    fecha = models.DateTimeField(auto_now_add=True, blank=True)
    tipo_pago = models.CharField(max_length= 13, choices=tipo_pago_option, default='Efectivo')
    cantidad = models.IntegerField(default=0)

    def __str__(self):
        return self.tipo_pago
