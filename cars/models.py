from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Car(models.Model):

    BRAND=(
        ("1","BMW"),
        ("2","AUDI"),
        ("3","VOLKSWAGEN"),
    )
    MODEL=(
        ("1","X5"),
        ("2","X6"),
        ("3","X7"),
        ("4","A5"),
        ("5","A7"),
        ("6","A8"),
        ("7","Polo"),
        ("8","Golf"),
        ("9","Passat"),

    )
    YEAR=(
        (1,"2021"),
        (2,"2022"),
        (3,"2023")
    )
    GEAR=(
        ("M","Manual"),
        ("A","Automatic"),
    )

    plate_number = models.CharField(max_length=15)
    brand = models.CharField(choices=BRAND, max_length=1, default=1)
    model = models.CharField(choices=MODEL, max_length=1, default=3)
    year = models.PositiveIntegerField(choices=YEAR, default=3)
    gear = models.CharField(choices=GEAR, max_length=1, default="A")
    rent_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.brand} {self.model} - {self.plate_number}"
    

class Reservation(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    customer = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # Kiralama yapıldığında aracın availability'sini False olarak güncelle
        self.car.availability = False
        self.car.save()
        super(Reservation, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        self.car.availability = True
        self.car.save()
        super(Reservation, self).delete(*args, **kwargs)
    
    def __str__(self):
        return f"Reservation for {self.car} by {self.customer} from {self.start_date} to {self.end_date}"

#!Customer = User 



