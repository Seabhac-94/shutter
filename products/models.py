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
    Irishness = 'Irishness'
    Nature = 'Nature'
    Still_Life = 'Still Life'
    Adventure = 'Adventure'

    PRODUCT_TYPE = (
        (Still_Life, 'Still Life'),
        (Adventure, 'Adventure'),
        (Nature, 'Nature'),
        (Irishness, 'Irishness')
    )
    name = models.CharField(max_length=254, default='')
    author = models.CharField(max_length=30, default='')
    description = models.TextField()
    photo_type = models.CharField(max_length=100, choices=PRODUCT_TYPE, default=Still_Life)
    available_in = models.CharField(max_length=20, choices=AVAILABLE_IN, default=Gloss)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.CharField(max_length=30, default='')
    image = models.ImageField(upload_to='images')
    tags = models.CharField(max_length=100, default='photography')
    port_or_land = models.CharField(max_length=100, choices=SIZE_TYPE, default=Portrait)
    product_id = models.CharField(max_length=20, default='shutter#')

    class Meta:
        ordering = ['photo_type']

    def __str__(self):
        return self.name
    