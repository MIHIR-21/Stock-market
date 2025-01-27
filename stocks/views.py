from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Add_stocks
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='stocks:login_page')
def home(request):
    stocks = Add_stocks.objects.all()
    context = {'stocks': stocks}
    return render(request, 'home.html', context)


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.info(request, 'Wellcome back buddy!')
            return redirect('stocks:home')
        else:
            messages.info(request, 'Username or Password is incorrect')

    return render(request, 'login.html')

def logout_page(request):
    print("hello")
    logout(request)
    messages.info(request, 'You have successfully logged out!')
    return redirect('stocks:login_page')

def register_page(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('stocks:register_page')

        
        user = User.objects.create(
            first_name = firstname,
            last_name = lastname,
            username = username,
            )
        
        user.set_password(password)
        user.save()

        messages.success(request, "Registration successful! Please log in.")
        return redirect('stocks:login_page')
    
    return render(request, 'register.html')


def add_stock(request):
    if request.method == 'POST':
        stockname = request.POST.get('stockname')
        stockprice = request.POST.get('stockprice')
        mrkcap = request.POST.get('mrkcap')
        
        # Add stock to database
        if stockname and stockprice and mrkcap:
            stock = Add_stocks(stockname=stockname, stockprice=stockprice , mrkcap=mrkcap)
            stock.save()

        messages.success(request, "Stock added successfully!")
        return redirect('stocks:home')
    

    return render(request, 'addstock.html')