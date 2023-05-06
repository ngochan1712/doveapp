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
class TODO(models.Model):
    vieccanlam1=models.CharField(max_length=40)
    vieccanlam2=models.CharField(max_length=40)
    vieccanlam3=models.CharField(max_length=40)
    vieccanlam4=models.CharField(max_length=40)
    
    
class personalin_fo(models.Model):
    firstname=models.CharField(max_length=40)
    lastname=models.CharField(max_length=40)
    lop=models.CharField(max_length=40)
    truong=models.CharField(max_length=40)
    gioitinh=models.CharField(max_length=40,null=True)
    place=models.CharField(max_length=40,null=True)
class my_goal(models.Model):
    shorttermgoal1=models.CharField(max_length=40)
    shorttermgoal2=models.CharField(max_length=40)
    shorttermgoal3=models.CharField(max_length=40)
    shorttermgoal4=models.CharField(max_length=40)
    shorttermgoal5=models.CharField(max_length=40)
    longtermgoal1=models.CharField(max_length=40)
    date1=models.DateTimeField(null=True)
    longtermgoal2=models.CharField(max_length=40)
    date2=models.DateTimeField(null=True)
    longtermgoal3=models.CharField(max_length=40)
    date3=models.DateTimeField(null=True)
    longtermgoal4=models.CharField(max_length=40)
    date4=models.DateTimeField(null=True)
    longtermgoal5=models.CharField(max_length=40)
    date5=models.DateTimeField(null=True)
   
