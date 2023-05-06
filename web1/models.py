from django.db import models

# Create your models here.
class Users(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    ten=models.CharField(max_length=30)

class Diem(models.Model):
    diemvan=models.FloatField(default=0)
    diemtoan=models.FloatField(default=0)
    diemanh=models.FloatField(default=0)
    diemhoa=models.FloatField(default=0)
    diemsinh=models.FloatField(default=0)
    diemly=models.FloatField(default=0)
    diemsu=models.FloatField(default=0)
    diemdia=models.FloatField(default=0)
    diemcongnghe=models.FloatField(default=0)
    diemgdcd=models.FloatField(default=0)
    user=models.ForeignKey(Users,to_field='id',on_delete=models.CASCADE)
class Todo(models.Model):
    vieccanlam1=models.CharField(max_length=40)
    vieccanlam2=models.CharField(max_length=40)
    vieccanlam3=models.CharField(max_length=40)
    vieccanlam4=models.CharField(max_length=40)
    vieccanlam4=models.CharField(max_length=40)
class personal_info(models.Model):
    firstname=models.CharField(max_length=40)
    lastname=models.CharField(max_length=40)
    lop=models.CharField(max_length=40)
    truong=models.CharField(max_length=40)
    
    