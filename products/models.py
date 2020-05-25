from django.db import models

# Create your models here.

class Product(models.Model):
    Gloss = 'Gloss'
    Canvas = 'Canvas'
    Framed = 'Framed'
    AVAILABLE_IN = (
        (Gloss, 'Gloss'),
        (Canvas, 'Canvas'),
        (Framed, 'Framed')
    )
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    available_in = models.CharField(max_length=20, choices=AVAILABLE_IN, default=Gloss)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.CharField(max_length=30, default='')
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
    