from django.db import models

# Create your models here.
class Users(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    ten=models.CharField(max_length=30)

class Diem(models.Model):
    diemvan=models.FloatField()
    diemtoan=models.FloatField()
    diemanh=models.FloatField()
    diemhoa=models.FloatField()
    diemsinh=models.FloatField()
    diemly=models.FloatField()
    diemsu=models.FloatField()
    diemdia=models.FloatField()
    diemcongnghe=models.FloatField()
    diemgdcd=models.FloatField()
    user=models.ForeignKey(Users,to_field='id',on_delete=models.CASCADE)
    

