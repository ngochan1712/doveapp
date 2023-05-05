
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from web1.forms import RegistrationForm
from web1.models import Users, Diem
# Create your views here.
def home(request):
    return render(request,'web1/home.html')
def base(request):
    return render(request,'web1/base.html')
def login(request):
    return render(request,'web1/login.html')
@csrf_exempt
def diemtb(request):
    data = None
    if request.method == 'POST':
        diemvan = request.POST['diemvan']
        diemtoan = request.POST['diemtoan']
        diemhoa = request.POST['diemhoa']
        
        Diem_TB = Diem(
            diemvan=diemvan,
            diemtoan=diemtoan,
            diemhoa=diemhoa,
            
        )
        diem_nhap = {
            'diemvan': diemvan,
            'diemtoan': diemtoan,
            'diemhoa': diemhoa,

        }
        Diem_TB.save()
        tb_10_mon = (diemvan + diemhoa + diemtoan)/3
        data = {'diemtrungbinh': tb_10_mon, 'data': diem_nhap}
        return render(request, 'web1/diemtb.html', data)
           
           
    return render(request,'web1/diemtb.html', data)
@csrf_exempt
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        name = request.POST['name']
        new_user = Users(
            username=username,
            password=password,
            ten=name,
        )
        new_user.save()
        return redirect('login/')     
           
           
    return render(request,'web1/signup.html')



