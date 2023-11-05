import datetime
from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(blank=False, null=True, max_length=50)
    apellido = models.CharField(blank=False, null=True,max_length=50)
    cedula = models.CharField(max_length=50, blank=False, null=True,)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    persona = models.ForeignKey(Persona,on_delete=models.CASCADE)
    activa = models.BooleanField(default=True)
    fecha_nacimiento = models.DateField(max_length=30)
    direccion = models.CharField(max_length=30)

    creado_el = models.DateField()
    actualizado_el=models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # Personalized form of update dateTime fields
        if not self.id:
            # Model without id.
            self.creado_el = datetime.datetime.now(datetime.timezone.utc)
        self.actualizado_el = datetime.datetime.now(datetime.timezone.utc)
        return super(Cliente, self).save(*args, **kwargs)


class TiposCuentas(models.Model):
    TIPO_CUENTA_AHORRO ="AHORRO"
    TIPO_CUENTA_CORRIENTE ="CORRIENTE"

    TIPO_CUENTA_CHOICES = (
        (TIPO_CUENTA_AHORRO, "AHORRO"),
        (TIPO_CUENTA_CORRIENTE, "CORRIENTE")
    )
    tipo_cuenta = models.CharField(choices=TIPO_CUENTA_CHOICES,max_length=50,default=TIPO_CUENTA_AHORRO, blank=True, null=True)
    descripcion = models.CharField(max_length=30)

class Cuentas(models.Model):
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    tipo_cuenta = models.ForeignKey(TiposCuentas,on_delete=models.CASCADE)
    activa = models.BooleanField(default=True)
    saldo = models.IntegerField(blank=True, null=True)
    creado_el = models.DateField(blank=True, null=True)
    actualizado_el=models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # Personalized form of update dateTime fields
        if not self.id:
            # Model without id.
            self.creado_el = datetime.datetime.now(datetime.timezone.utc)
        self.actualizado_el = datetime.datetime.now(datetime.timezone.utc)
        return super(Cuentas, self).save(*args, **kwargs)

class Movimientos(models.Model):
    TIPO_MOVIMIENTO_DEPOSITO ="DEPOSITO"
    TIPO_MOVIMIENTO_RETIRO ="RETIRO"
    TIPO_MOVIMIENTO_TRANSFERENCIA ="TRANSFERENCIA"
    TIPO_MOVIMIENTO_PAGO ="PAGO"
    TIPO_MOVIMIENTO_INTERESES ="INTERESES"
    TIPO_MOVIMIENTO_AJUSTES ="AJUSTES"

    TIPO_MOVIMIENTO_CHOICES = (
        (TIPO_MOVIMIENTO_DEPOSITO, "DEPOSITO"),
        (TIPO_MOVIMIENTO_RETIRO, "RETIRO"),
        (TIPO_MOVIMIENTO_TRANSFERENCIA, "TRANSFERENCIA"),
        (TIPO_MOVIMIENTO_PAGO, "PAGO"),
        (TIPO_MOVIMIENTO_INTERESES, "INTERESES"),
        (TIPO_MOVIMIENTO_AJUSTES, "AJUSTES")
    )
    cuenta = models.ForeignKey(Cuentas,on_delete=models.CASCADE)
    tipo_movimiento = models.CharField(choices=TIPO_MOVIMIENTO_CHOICES,max_length=50)
    monto  = models.IntegerField()
    actualizado_el = models.DateField()

    def save(self, *args, **kwargs):
        # Personalized form of update dateTime fields
        self.actualizado_el = datetime.datetime.now(datetime.timezone.utc)
        return super(Movimientos, self).save(*args, **kwargs)
