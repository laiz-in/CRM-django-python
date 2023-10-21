from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from .forms import SignUpForm

# Create  view for home page
def home(request):
    # Check to see if logging in
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username , password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"you have succesfully logged in!")
            return redirect('home')
        else:
            messages.success(request, "Error loggin in, please try again!")
            return redirect('home')
    else:
        return render(request,'home.html',{})


# If we need to craete a seperate log in view
def login_user(request):
    pass

# Create a log out view
def logout_user(request):
    logout(request)
    messages.success(request,"you have logged out!")
    return redirect('home')


# Create a register user view
def register_user(request):
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and log in
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username="username", password= "password1")
            login(request, user)
            messages.success(request,"You have sucessfully Registred!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})

    return render(request, 'register.html', {'form':form})













