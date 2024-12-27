from django.db import models
from django.core.exceptions import ValidationError


def validate_image(image):
    file_size = image.file.size
    limit_kb = 500
    if file_size > limit_kb * 1024:
        raise ValidationError(f"El tamaño máximo permitido para las imágenes es {limit_kb}KB.")
    if not image.name.lower().endswith(('.png', '.jpg', '.jpeg')):
        raise ValidationError("Solo se permiten imágenes en formato PNG, JPG o JPEG.")
    

class Product(models.Model):
    """
    representa un producto del catalogo
    """
    name = models.CharField("Nombre", max_length=200)
    description = models.TextField("Descripción", max_length=500)
    product_image = models.ImageField(upload_to='products/images/', validators=[validate_image], blank=True, null=True)
    code=models.CharField("Código", max_length=50, unique=True, blank=True, null=True)

    def __str__(self):
        return f"{self.code} - {self.name}"

    class Meta:
         verbose_name="Producto"
         verbose_name_plural="Productos"


class Order(models.Model):
    orden_date = models.DateField("Fecha de orden")
    description = models.TextField("Descripción", max_length=500)

    def __str__(self):
        return f"{self.orden_date} - {self.description}"

    class Meta:
         verbose_name="Orden de compra"
         verbose_name_plural="Ordenes de compra"



class Packaged(models.Model):
    name = models.CharField("Nombre", max_length=200)
    amount = models.IntegerField("Cantidad")

    def __str__(self):
        return f"{self.name}"

    class Meta:
         verbose_name="Paquete"
         verbose_name_plural="Paquetes"


class Inventory(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete= models.PROTECT, 
        null=False,
        blank=False,
        verbose_name="Orden de compra"
    )
    product = models.ForeignKey(
        Product,
        on_delete= models.PROTECT, 
        null=False,
        blank=False,
        verbose_name="Producto"
    )
    amount = models.IntegerField("Cantidad")
    purchase_price = models.FloatField("Precio de compra")#agregar foranea de orden

    def __str__(self):
        return f"{self.product.name} - {self.amount} - ${self.purchase_price/self.amount}"

    class Meta:
         verbose_name="Inventario"
         verbose_name_plural="Inventario"

class Price(models.Model):
    inventory = models.ForeignKey(
        Inventory,
        on_delete= models.PROTECT, 
        null=False,
        blank=False,
        verbose_name="Inventario"
    )
    packaged = models.ForeignKey(
        Packaged,
        on_delete = models.PROTECT, 
        null = False,
        blank = False,
        verbose_name = "Paquete"
    )
    sale_price = models.FloatField("Precio de venta")

    def __str__(self):
        return f"{self.inventory.product.name} - {self.packaged.name}"

    class Meta:
         verbose_name="Precio"
         verbose_name_plural="Precios"