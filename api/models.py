from django.db import models

class Location(models.Model):
    locationName = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.locationName


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    data_added = models.DateField(auto_now_add = True)
    ItemName = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
