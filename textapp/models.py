
from django.db import models
from django.contrib.auth.models import AbstractUser



class Userregistration(models.Model):
    # user=models.OneToOneField(Login,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    
    uname=models.CharField(max_length=50,null=True)
    dob=models.DateField(null=True)
    img=models.ImageField(upload_to="profile",null=True)

class Driver(models.Model):
    dname=models.CharField(max_length=100,blank=True)
    daddress=models.CharField(max_length=100,blank=True)
    dcontact=models.CharField(max_length=100,blank=True)
    demail=models.CharField(max_length=100,blank=True)
    dpassword=models.CharField(max_length=100,blank=True)
    status=models.CharField(max_length=100,blank=True)


class Login(models.Model):
    username=models.CharField(max_length=100,blank=True)
    password=models.CharField(max_length=100,blank=True)
    usertype=models.CharField(max_length=100,blank=True)
    status=models.CharField(max_length=100,blank=True)
    driverid=models.ForeignKey(Driver,null=True,on_delete=models.CASCADE)



class User(models.Model):
    uname=models.CharField(max_length=100,blank=True)
    uaddress=models.CharField(max_length=100,blank=True)
    ucontact=models.CharField(max_length=100,blank=True)
    uemail=models.CharField(max_length=100,blank=True)
    upassword=models.CharField(max_length=100,blank=True)


class Booking(models.Model):
    uid=models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    did=models.ForeignKey(Driver,null=True,on_delete=models.CASCADE)
    date=models.CharField(max_length=100,blank=True)
    status=models.CharField(max_length=100,blank=True)
    
