from django.db import models

# Create your models here.

class Studentinfo(models.Model):
    studentid = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    studentmajor = models.CharField(max_length=100)
    studentyear = models.CharField(max_length=100)
    gpa = models.DecimalField(max_digits=2, decimal_places=1)

class Courseinfo(models.Model):
    courseid = models.IntegerField(primary_key=True)
    coursetitle = models.CharField(max_length=100)
    coursename = models.CharField(max_length=100)
    coursecode = models.IntegerField()
    coursedep = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100) 
