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
def register(request):
    return render(request,'web1/register.html')
@csrf_exempt
def signup(request):
    if request.method == 'POST':
        registrationForm = RegistrationForm(request.POST)
        print(registrationForm)
        if registrationForm.is_valid():
            username = registrationForm.cleaned_data['username']
            
            print(username)
           
    return render(request,'web1/signup.html')

from django.shortcuts import render
from .forms import RegistrationForm
from django.http import HttpResponse
def index(request):
    return render(request, 'pages/home.html')
def contact(request):
    return render(request,'pages/contact.html')
def error(request):
    return render(request,'pages/error.html')
def register(request):
    form = RegistrationForm()



