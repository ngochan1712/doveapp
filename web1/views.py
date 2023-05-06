
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from web1.forms import RegistrationForm
from web1.models import Users, Diem, TODO, personalin_fo, my_goal

# Create your views here.
def home(request):
    return render(request,'web1/home.html')
@csrf_exempt
def mygoal(request):
     if request.method == 'POST':
        shorttermgoal1 = request.POST['shorttermgoal1']
        shorttermgoal2 = request.POST['shorttermgoal2']
        shorttermgoal3 = request.POST['shorttermgoal3']
        shorttermgoal4 = request.POST['shorttermgoal4']
        shorttermgoal5 = request.POST['shorttermgoal5']
        longtermgoal1=request.POST['longtermgoal1']
        longtermgoal2=request.POST['longtermgoal2']
        longtermgoal3=request.POST['longtermgoal3']
        longtermgoal4=request.POST['longtermgoal4']
        longtermgoal5=request.POST['longtermgoal5']
        date1=request.POST['date1']
        date2=request.POST['date2']
        date3=request.POST['date3']
        date4=request.POST['date4']
        date5=request.POST['date5']
        mygoals= my_goal(
           shorttermgoal1=shorttermgoal1,
           shorttermgoal2=shorttermgoal2,
           shorttermgoal3=shorttermgoal3,
           shorttermgoal4=shorttermgoal4,
           shorttermgoal5=shorttermgoal5,
           longtermgoal1=longtermgoal1,
           longtermgoal2=longtermgoal2,
           longtermgoal3=longtermgoal3,
           longtermgoal4=longtermgoal4,
           longtermgoal5=longtermgoal5,
           date1=date1,
           date2=date2,
           date3=date3,
           date4=date4,
           date5=date5,
        )
        mygoals.save()
     return render(request,'web1/mygoal.html')
@csrf_exempt
def personal_info(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        truong = request.POST['truong']
        lop = request.POST['lop']
        gioitinh= request.POST['gioitinh']
        place=request.POST['place']
        personalinfo= personalin_fo(
            firstname=firstname,
            lastname=lastname,
            lop=lop,
            truong=truong,
            gioitinh=gioitinh,
            place=place,
            
        )
        personalinfo.save()
     
    return render(request,'web1/personal_info.html')
@csrf_exempt
def todolist(request):
     if request.method == 'POST':
        vieccanlam1 = request.POST['vieccanlam1']
        vieccanlam2 = request.POST['vieccanlam2']
        vieccanlam3 = request.POST['vieccanlam3']
        vieccanlam4 = request.POST['vieccanlam4']

        Todo = TODO(
            vieccanlam1=vieccanlam1,
            vieccanlam2=vieccanlam2,
            vieccanlam3=vieccanlam3,
            vieccanlam4=vieccanlam4,
            
            
        )
        Todo.save()
     return render(request,'web1/todolist.html')
def signup(request):
    return render(request,'web1/signup.html')
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
def login(request):
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
        return redirect('home')     
           
           
    return render(request,'web1/login.html')



