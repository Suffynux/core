from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()
    email = models.EmailField()
    text = models.TextField()

class product(models.Model):
    pass
class Car(models.Model):
    car_name= models.CharField(max_length=500)
    car_speed = models.IntegerField()
    
    def __str__(self) -> str:
        return self.car_name  