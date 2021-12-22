from django.db import models
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

# Create your models here.]
class Register(models.Model):
    Title = models.CharField(max_length=200, null=True, blank=True)
    First_Name = models.CharField(max_length=250, null=True, blank=True)
    Last_Name = models.CharField(max_length=250, null=True, blank=True)
    Email = models.EmailField(max_length=254, null=True, blank=True)
    Password1 = models.CharField(max_length=100, null=True, blank=True)
    Password2 = models.CharField(max_length=100, null=True, blank=True)
    DOB = models.DateField(null=True, blank=True)
    Company = models.CharField(max_length=100, null=True, blank=True)
    Address = models.CharField(max_length=500, null=True, blank=True)
    Address2 = models.CharField(max_length=500, null=True, blank=True)
    City = models.CharField(max_length=100, null=True, blank=True)
    State = models.CharField(max_length=200, null=True, blank=True)
    Zip_Code = models.CharField(max_length=20, null=True, blank=True)
    Country = models.CharField(max_length=250,null=True, blank=True)
    #Country = CountryField(null=True, blank=True)
    Additional_Info = models.TextField(null=True, blank=True)
    Home_Phone= PhoneNumberField(null=True, blank=True)
    Mobile_Phone = PhoneNumberField(null=True, blank=True)

    
    def __str__(self):
        return self.First_Name

