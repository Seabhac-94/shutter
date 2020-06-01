from django.db import models

# Create your models here.

class Product(models.Model):
    """
    A product
    """
    """
    Product has multiple possibilities, such has framed type and size.
    """
    Gloss = 'Gloss'
    Canvas = 'Canvas'
    Framed = 'Framed'
    AVAILABLE_IN = (
        (Gloss, 'Gloss'),
        (Canvas, 'Canvas'),
        (Framed, 'Framed')
    )
    Landscape = 'Landscape'
    Portrait = 'Portrait'
    SIZE_TYPE = (
        (Landscape, 'Landscape'),
        (Portrait, 'Portrait')
    )
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    available_in = models.CharField(max_length=20, choices=AVAILABLE_IN, default=Gloss)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.CharField(max_length=30, default='')
    image = models.ImageField(upload_to='images')
    port_or_land = models.CharField(max_length=100, choices=SIZE_TYPE, default=Portrait)
    product_id = models.CharField(max_length=20, default='shutter#')

    def __str__(self):
        return self.name
    