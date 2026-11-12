from django.db import models
from django.contrib.auth.models import User

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    mileage = models.IntegerField()

    seller = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)

    class Meta:
        indexes = [
            models.Index(fields = ["price"]),]