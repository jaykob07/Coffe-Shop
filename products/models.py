from django.db import models


# Create your models here.
class Products(models.Model):
    name = models.TextField(max_length=200, verbose_name="nomnbre")
    descripcion = models.TextField(max_length=300, verbose_name="descripcion")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="precio")
    avalible = models.BooleanField(default=True, verbose_name="disponible")
    photo = models.ImageField(upload_to="logos", null=True, blank=True, verbose_name="foto")


    def __str__(self):
        return self.name