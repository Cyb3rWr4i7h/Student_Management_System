from django.shortcuts import render
from datetime import datetime
from sms.models import Help
from django.contrib import messages

# Create your views here.

def dashboard(request):
    return render(request, "home.html")

def login(request):
    return render(request, "login.html")

def help(request):
    if request.method == "POST":
        userID = request.POST.get("userID")
        email = request.POST.get("email")
        problem = request.POST.get("problem")
        # help = Help(userID="userID", email="email", problem="problem", date=datetime.today())
        # help = Help(userID, email, problem, date=datetime.today())
        help = Help(userID=userID, email=email, problem=problem, date=datetime.today())
        help.save()
        messages.success(request, "Your Problem has been Recorded.")
    return render(request, "help.html")

def signup(request):
    return render(request, 'signup.html')
