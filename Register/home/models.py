from django.db import models

# Create your models here.
class Register(models.Model):
    First_Name=models.CharField(max_length=50)
    Last_Name=models.CharField(max_length=50)
    Address=models.CharField(max_length=50)
    Phone_Number=models.CharField(max_length=15)
    Email=models.CharField(max_length=100)
    Collage_Name=models.CharField(max_length=100)
    Gender=models.CharField(max_length=10)
    Area_Of_Intrest=models.CharField(max_length=100)

    def __str__(self):
        return self.First_Name