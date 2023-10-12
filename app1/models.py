from django.db import models


# Create your models here.

#This is the model for the flower type
class type(models.Model):

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    

#This is the model for the flower color  
class color(models.Model):

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


#This is the model for the inventory of flowers
class Inventory(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(type, on_delete=models.CASCADE)
    color = models.ForeignKey(color, on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.CharField(max_length=300)

    # Add a field to store Firestore document ID
    firestore_document_id = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name
    

class Customer(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=12)
    address = models.CharField(max_length=300)

    def __str__(self):
        return self.name


