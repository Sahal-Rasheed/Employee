from django.db import models

# Create your models here.

class Designation(models.Model):
    designation = models.TextField()

    def __str__(self):
        return self.designation

class Employee(models.Model):
    name        = models.CharField(max_length=100)
    email       = models.EmailField(max_length=70, unique=True)
    address     = models.CharField(max_length=250)
    photo       = models.ImageField(upload_to='profilepic', blank=True)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)

    def __str__(self):
        return self.name