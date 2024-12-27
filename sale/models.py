from django.db import models
from inventory.models import Price

class Sale(models.Model):
    """
    representa una venta
    """
    precio = models.ForeignKey(
        Price,
        on_delete = models.PROTECT, 
        null = False,
        blank = False,
        verbose_name = "Producto"
        
    )
    amount = models.IntegerField("Cantidad")
    sale_date = models.DateField("Fecha de venta")


    def __str__(self):
        return f"{self.amount} - {self.sale_date}"

    class Meta:
         verbose_name="Venta"
         verbose_name_plural="Ventas"
