from urllib import request
from django.shortcuts import render, redirect
from .models import Notify
# Create your views here.
def home(request):
    return render(request, "home.html")

def team(request):
    return render(request, "team.html")

def trial2(request):
    return render(request, "trial2.html")

# def notify(request):
#     if request.method == "POST":
#         email = request.POST.get('email','')
#         response = Notify(email=email)
#         response.save()
#     return redirect('home')


def home(request):
    is_not_home = 0
    return render(request, "home.html",
                  {
                      "is_not_home": is_not_home
                  }
                  )
    
    
def notify(request):
    is_not_home = 1
    if request.method == "POST":
        is_exists = 0
        message = ""
        name = request.POST.get('name', '')
        colg = request.POST.get('colg', '')
        email = request.POST.get('email', '')
        contact = request.POST.get('contact', '')
        address = request.POST.get('address', '')
        is_filled = (len(Notify.objects.filter(email=email))==1) or (len(Notify.objects.filter(contact=contact))==1)
        if is_filled:
            message = "email or phone number already exists"
            is_exists = 1
        else:
            message = "You have submitted successfully"
            response = Notify(email=email, name=name, colg=colg, address=address, contact=contact)
            response.save()
    return render(request, 'home.html',
                  {
                      'message': message,
                      "is_exists": is_exists,
                       "is_not_home": is_not_home
                  }
                  )
