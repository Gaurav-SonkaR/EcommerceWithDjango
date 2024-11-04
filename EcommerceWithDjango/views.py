from django.http import HttpResponse
from django.shortcuts import render,redirect

def home(request):
    return render(request,"index.html")

def login(request):
    data ={}
    try:   
        if request.method == "POST":
                email = request.POST.get('email')
                password = request.POST.get('password')
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
        if request.method == "POST":
            full_name = request.POST.get('full_name')
            email = request.POST.get('email')
            country_code = request.POST.get('country_code')
            phone = request.POST.get('phone')
            dob = request.POST.get('dob')
            gender = request.POST.get('gender')
            password = request.POST.get('password')
            # confirm_password = request.POST.get('confirm_password')
            address = request.POST.get('address')
            city = request.POST.get('city')
            state = request.POST.get('state')

            data={
                'full_name' : full_name,
                'email' : email,
                'country_code' : country_code,
                'phone' : phone,
                'dob' : dob,
                'gender' : gender,
                'password' : password,
                # 'confirm_password' : confirm_password,
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