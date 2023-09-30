from django.db import models

# Create your models here.
class Receipe(models.Model):
    receipe_name = models.CharField(max_length=100)  # Adjusted max_length to 100 or any suitable value
    receipe_description = models.TextField()
    receipe_img = models.ImageField()
