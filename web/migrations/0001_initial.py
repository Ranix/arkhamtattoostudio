# Generated by Django 2.0.4 on 2018-06-17 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('nombre', models.CharField(max_length=128)),
                ('telefono', models.CharField(max_length=10)),
                ('correo', models.EmailField(max_length=254)),
                ('zona', models.CharField(choices=[('Torso/Espalda', '1.- TORSO/ESPALDA'), ('Brazo', '2.- BRAZO'), ('Antebrazo', '3.- ANTEBRAZO'), ('Muslo', '4.- MUSLO'), ('Pierna Baja', '5.- PIERNA BAJA'), ('Pie', '6.- PIE'), ('Cuello', '7.- CUELLO'), ('Manos', '8.- MANOS'), ('Cabeza', '9.- CABEZA'), ('Cadera', '10.- CADERA')], default='Torso/Espalda', max_length=17)),
                ('tinta', models.CharField(choices=[('Escala grises', 'Escala de grises'), ('Color', 'Color'), ('Costado interior', 'Costado interior'), ('Costado exterior', 'Costado exterior')], default='escala', max_length=16)),
                ('posicion', models.CharField(choices=[('Frente', 'FRENTE'), ('Posterior', 'POSTERIOR')], default='frente', max_length=9)),
                ('alto', models.IntegerField()),
                ('ancho', models.IntegerField()),
                ('referencia1', models.ImageField(blank=True, null=True, upload_to='')),
                ('referencia2', models.ImageField(blank=True, null=True, upload_to='')),
                ('referencia3', models.ImageField(blank=True, null=True, upload_to='')),
                ('descripcion', models.TextField(default='', max_length=280)),
                ('no_horas', models.IntegerField(default=0)),
                ('anticipo', models.IntegerField(choices=[(200, 200), (500, 500)], default=200)),
                ('precioTotal', models.IntegerField(default=0)),
                ('comentarios', models.TextField(default='', max_length=280)),
                ('cotizado', models.BooleanField(default=False)),
            ],
        ),
    ]
