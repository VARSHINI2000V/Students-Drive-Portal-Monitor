from django.db import models
from django.db.models.fields import CharField, DateField, IntegerField

# Create your models here.

class students(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    Password=models.CharField(max_length=50)
    rollno=models.CharField(max_length=10)
    Address=models.CharField(max_length=100)
    state=models.CharField(max_length=15)
    country=models.CharField(max_length=15)
    email=models.CharField(max_length=50)
    dob=models.DateField()
    contact=models.CharField(max_length=10)
    dept=models.CharField(max_length=20)
    year=models.CharField(max_length=50)
    cgpa=models.IntegerField()
    backlogs=models.IntegerField(default=0)
    placed=models.CharField(max_length=20,default="NO")


class studentplaced(models.Model):
    name=models.CharField(max_length=100)
    rollno=models.CharField(max_length=100,default="rollno")
    email=models.CharField(max_length=100,default="email")
    programme=models.CharField(max_length=100,default="NO")
    bond=models.IntegerField(default=0)
    ftepackage=models.CharField(max_length=50)
    fulltime=models.CharField(max_length=50)
    intern=models.CharField(max_length=50)
    internpack=models.CharField(max_length=50)
    role=models.CharField(default="role",max_length=255)
    image=models.FileField(default='defaults.jpg')


class admin(models.Model):
    name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)


class companies(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    bond=models.IntegerField(default=0)
    fte=models.CharField(max_length=20)
    intern=models.CharField(max_length=20)
    ftepack=models.CharField(max_length=10)
    internpack=models.CharField(max_length=10)
    programme=models.CharField(max_length=200)
    PG=models.IntegerField()
    date=models.DateField(auto_now=True)
    link=models.CharField(max_length=500,default="NOLINK")
    role=models.CharField(default="role",max_length=255)

class registeration(models.Model):
    email=models.CharField(max_length=255,default="email")
    rollno=models.CharField(max_length=255,default=0)
    date=models.DateField(auto_now=True)
    companyname=models.CharField(max_length=255)
    status=models.CharField(max_length=255)
    programme=models.CharField(default="programme",max_length=255)

class staff(models.Model):
    name=models.CharField(max_length=255)
    dept=models.CharField(max_length=255)
    password=models.CharField(max_length=255)



