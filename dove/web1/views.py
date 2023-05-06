
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from web1.forms import RegistrationForm
from web1.models import Users, Diem, Todo

# Create your views here.
def home(request):
    return render(request,'web1/home.html')
def personal_info(request):
    return render(request,'web1/personal_info.html')
@csrf_exempt
def todolist(request):
     if request.method == 'POST':
        vieccanlam1 = request.POST['vieccanlam1']
        vieccanlam2 = request.POST['vieccanlam2']
        vieccanlam3 = request.POST['vieccanlam3']
        vieccanlam4 = request.POST['vieccanlam4']
        vieccanlam5 = request.POST['vieccanlam5']
        Todo = Todo(
            vieccanlam1=vieccanlam1,
            vieccanlam2=vieccanlam2,
            vieccanlam3=vieccanlam3,
            vieccanlam4=vieccanlam4,
            vieccanlam5=vieccanlam5,
        )
        Todo.save()
     return render(request,'web1/todolist.html')
def login(request):
    return render(request,'web1/login.html')
@csrf_exempt
def diemtb(request):
    data = None
    if request.method == 'POST':
        diemvan = request.POST['diemvan']
        diemtoan = request.POST['diemtoan']
        diemhoa = request.POST['diemhoa']
        diemanh = request.POST['diemanh']
        diemsu = request.POST['diemsu']
        diemsinh = request.POST['diemsinh']
        diemcongnghe = request.POST['diemcongnghe']
        diemdia = request.POST['diemdia']
        diemgdcd = request.POST['diemgdcd']
        diemly = request.POST['diemly']
        
       
        
        Diem_TB = Diem(
            diemvan=diemvan,
            diemtoan=diemtoan,
            diemhoa=diemhoa,
            diemanh=diemanh,
            diemsu=diemsu,
            diemdia=diemdia,
            diemgdcd=diemgdcd,
            diemcongnghe=diemcongnghe,
            diemsinh=diemsinh,
            diemly=diemly,
            user_id=1,
        )
        diem_nhap = {
            'diemvan': diemvan,
            'diemtoan': diemtoan,
            'diemhoa': diemhoa,
            'diemanh': diemanh,
            'diemsu': diemsu,
            'diemdia': diemdia,
            'diemgdcd': diemgdcd,
            'diemcongnghe': diemcongnghe,
            'diemly': diemly,
            'diemsinh': diemsinh,


           
           
        }
        Diem_TB.save()
        tb_10_mon = (float(diemvan) + float(diemhoa) + float(diemtoan)+float(diemanh)+float(diemly)+ float(diemsu) + float(diemgdcd)+float(diemgdcd) + float(diemsinh) + float(diemdia) )/10
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



