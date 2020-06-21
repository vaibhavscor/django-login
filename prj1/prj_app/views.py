from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm       # this is custom made form
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def loginpage(request):     # dont give name login       
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username, password=password)
        print(user)
        if user is not None:
            # ddfsfsf
            login(request,user)
            print( login(request,user))
            redirect('home')
    
    return render(request,'login.html')


def signup(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)   # posting to database 
        if form.is_valid():
            form.save() 
            user_name = form.cleaned_data.get('username')
            messages.success(request, "ACCOUNT CREATED For USERNAME " + user_name)
            return redirect('login')
    
    dicto = {'form':form}
    return render(request,'signup.html',dicto) 



def home(request):
    return render(request, 'home.html')
