from django.db import models

class admin(models.Model):
    name= models.CharField(max_length=200)
    email= models.EmailField(max_length=200, unique=True)
    password= models.CharField(max_length=200)

class user(models.Model):
    name= models.CharField(max_length=200)
    email= models.EmailField(max_length=200, unique=True)
    address= models.CharField(max_length=200)
    image= models.ImageField(upload_to="user",null=True)
    password= models.CharField(max_length=200)
    nationality= models.CharField(max_field=200)

