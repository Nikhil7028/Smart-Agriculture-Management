from django.db import models
# Create your models here.


class FarmerInfo(models.Model):
    fullname = models.CharField(max_length=100) 
    mobno = models.CharField(max_length=10)
    whatappsno = models.CharField(max_length=10)
    email = models.CharField(max_length=50,  blank=True, null=True)
    gender = models.CharField(max_length=10)
    village = models.CharField(max_length=30)
    dist = models.CharField(max_length=20)
    subdist = models.CharField(max_length=20)
    pincode = models.CharField(max_length=6,  blank=True, null=True)
    totalland = models.IntegerField(null=True)
    maincrop = models.CharField(max_length=90,  blank=True, null=True)
    irrigation = models.CharField(max_length=90, blank=True, null=True)
    password= models.CharField(max_length=20)  
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname
    
class worker(models.Model):
    fullName= models.CharField(max_length=100)
    age= models.IntegerField()
    gender= models.CharField(max_length=10)
    dist = models.CharField(max_length=20)
    subDist= models.CharField(max_length=20)
    village = models.CharField(max_length=30)    
    mobno = models.CharField(max_length=10, unique=True) 
    password= models.CharField(max_length=20)   
    skill= models.CharField(max_length=250,  blank=True, null=True)
    availabillity=models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

class contactUs(models.Model):
    Name= models.CharField(max_length=100)
    email= models.CharField(max_length=50, unique=True)
    phone= models.CharField(max_length=10) 
    message = models.CharField(max_length=290)
    checked= models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    






























class HireRequest(models.Model):
    farmer = models.CharField(max_length=100) 
    worker = models.ForeignKey(worker, on_delete=models.CASCADE)
    purpose = models.CharField(max_length=200)
    duration = models.PositiveIntegerField()
    location = models.CharField(max_length=200)
    f_mobno = models.CharField(max_length=10)
    hire_date = models.DateTimeField(auto_now_add=True)
    STATUS = models.CharField(max_length=200, default='pending')
    
