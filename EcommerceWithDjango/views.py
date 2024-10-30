from django.http import HttpResponse
from django.shortcuts import render,redirect

def home(request):
    return render(request,"index.html")

def login(request):
    data ={}
    try:   

                email = request.GET.get('email')
                password = request.GET.get('password')
                data={
                    'email':email,
                    'password':password,
                }
    except:
        pass
    return render(request,"login.html",data)

def register(request):
    data = {}
    try:
        # Suggested code may be subject to a license. Learn more: ~LicenseLog:1856409913.
        full_name = request.GET.get('full_name')
        email = request.GET.get('email')
        country_code = request.GET.get('country_code')
        phone = request.GET.get('phone')
        dob = request.GET.get('dob')
        gender = request.GET.get('gender')
        password = request.GET.get('password')
        confirm_password = request.GET.get('confirm_password')
        address = request.GET.get('address')
        city = request.GET.get('city')
        state = request.GET.get('state')

        data={
            'full_name' : full_name,
            'email' : email,
            'country_code' : country_code,
            'phone' : phone,
            'dob' : dob,
            'gender' : gender,
            'password' : password,
            'confirm_password' : confirm_password,
            'address' : address,
            'city' : city,
            'state' : state,
        }
        print(data)
    except:
        pass
    return render(request,"register.html",data)

def cart(request):
    return render(request,"cart.html")