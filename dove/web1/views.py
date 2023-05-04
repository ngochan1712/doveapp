from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from web1.forms import RegistrationForm

# Create your views here.
def home(request):
    return render(request,'web1/home.html')
def base(request):
    return render(request,'web1/base.html')
def login(request):
    return render(request,'web1/login.html')
@csrf_exempt
def signup(request):
    if request.method == 'POST':
        registrationForm = RegistrationForm(request.POST)
        print(registrationForm)
        if registrationForm.is_valid():
            username = registrationForm.cleaned_data['username']
            
            print(username)
           
    return render(request,'web1/signup.html')



