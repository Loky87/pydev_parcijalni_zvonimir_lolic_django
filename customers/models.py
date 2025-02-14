from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=255)
    vat_id = models.CharField(max_length=11)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.name