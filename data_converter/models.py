from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_id = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    country = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    sub_date = models.DateField()
    website = models.CharField(max_length=50)