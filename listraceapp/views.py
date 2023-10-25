from django.shortcuts import render,redirect
from listraceapp.models import Article
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
# Create your views here.
def index(request):
    obj=Article.objects.all()
    return render(request,'index.html',{'result':obj})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken")
                return redirect('/register/')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already taken")
                return redirect('/register/')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                                email=email, last_name=last_name)
                user.save();
                return redirect('/login/')

        else:
            messages.info(request, "Passwords not matching")
            return redirect('/register/')
        return redirect('/')

    return render(request, "register.html")

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid login")
            return redirect('/login/')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')