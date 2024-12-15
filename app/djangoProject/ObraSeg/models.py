from django.db import models

# Create your models here.
class City(models.Model):
    name_city = models.CharField(max_length=100, verbose_name="Ciudad")

    def _str_(self):
        return self.name_city
    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"
        db_table = "city"
        ordering = ["id"]

class Customer(models.Model):
    names = models.CharField(max_length=150, verbose_name="Nombres")
    dni = models.CharField(max_length=13, verbose_name="Ruc o Cédula")
    email = models.CharField(max_length=150, verbose_name="Correo Electrónico")
    address = models.TextField(verbose_name="Dirección")
    phone = models.CharField(max_length=15, verbose_name="Teléfono")
    movil = models.CharField(max_length=15, verbose_name="Celular")
    avatar = models.ImageField(upload_to="avatar", verbose_name="Foto del Cliente", null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Modificación")
    def str(self):
        return self.names

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        db_table = "customer"
        ordering = ["id"]

class Cotizador(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_cotiza = models.DateField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Subtotal de la cotización")
    tax = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Monto del Impuesto")
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total de la cotización")
    state = models.CharField(max_length=50, choices=[
        ('Pendiente', 'Pendiente'),
        ('Aprobada', 'Aprobada'),
        ('Rechazada', 'Rechazada')
    ])
    comments = models.TextField(blank=True, null=True, verbose_name="Observaciones Adicionales")

    def _str_(self):
        return f'Cotización {self.id} - Cliente: {self.customer.name}'

    class Meta:
        verbose_name = "Cotización"
        verbose_name_plural = "Cotizaciones"
        db_table = "cotizador"
        ordering = ["id"]


