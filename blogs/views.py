from django.shortcuts import render, redirect
from .models import Popular
from .models import New
from .models import Cones
from .models import Sticks
from .models import Cake
from .models import Mochi
from .models import List
from .models import Cart
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def index(request):
    count = Cart.objects.all().count()
    data = Popular.objects.all()
    data2 = New.objects.all()
    context = {'posts':data, 'news':data2, 'count': count}
    return render(request, 'index.html', context)

def new(request):
    count = Cart.objects.all().count()
    data = New.objects.all()
    context = {'posts':data, 'count': count}
    return render(request, 'new.html', context)

def cones(request):
    count = Cart.objects.all().count()
    data = Cones.objects.all()
    data2 = New.objects.all()
    context = {'posts':data, 'news':data2, 'count': count}
    return render(request, 'cones.html', context)

def sticks(request):
    count = Cart.objects.all().count()
    data = Sticks.objects.all()
    data2 = New.objects.all()
    context = {'posts':data, 'news':data2, 'count': count}
    return render(request, 'sticks.html', context)

def cake(request):
    count = Cart.objects.all().count()
    data = Cake.objects.all()
    data2 = New.objects.all()
    context = {'posts':data, 'news':data2, 'count': count}
    return render(request, 'cake.html', context)

def mochi(request):
    count = Cart.objects.all().count()
    data = Mochi.objects.all()
    data2 = New.objects.all()
    context = {'posts':data, 'news':data2, 'count': count}
    return render(request, 'mochi.html', context)

def checkSearch(request):
    count = Cart.objects.all().count()
    check = 1
    context = {'checkSearch':check, 'count': count}
    return render(request, 'index.html',context)

def search(request):
    text = ''
    if 'text' in request.GET:
        text = request.GET['text']
        if text is '':
            data = ''
            check = 0
        else:
            data = List.objects.filter(name__icontains=text)
            count = List.objects.filter(name__icontains=text).count()
            if count == 0:
                check = 0
            else:
                check = 1
    else:
        check = 0
    Count = Cart.objects.all().count()
    data2 = New.objects.all()
    context = {'posts':data, 'news':data2, 'check':check, 'text':text, 'count': Count}
    return render(request, 'search.html', context)

def register(request):
    count = Cart.objects.all().count()
    return render(request, 'register.html', {'count': count})

def login(request):
    count = Cart.objects.all().count()
    return render(request, 'login.html', {'count': count})

def addUser(request):
    username = request.POST['username']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    password = request.POST['password']
    repassword = request.POST['repassword']
    
    if password == repassword:
        if User.objects.filter(username=username).exists():
            messages.error(request, 'The username has been used !')
            return redirect('/register')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'This email has been used !')
            return redirect('/register')
        elif len(password)<8:
            messages.error(request, 'Password must be 8 characters or more !')
            return redirect('/register')
        else:
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=firstname,
                last_name=lastname
            )   
            user.save()
            messages.success(request, 'Register complete !')
            return redirect('/login')
    else:
        messages.error(request, 'Confirm the password is incorrect !')
        return redirect('/register')

def userLogin(request):
    username = request.POST['username']
    password = request.POST['password']
    

    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request,user)
        messages.success(request, 'Login complete !')
        return redirect('/account')
    else:
        messages.error(request, "User or Password is incorrect !")
        return redirect('/login')

def account(request):
    count = Cart.objects.all().count()
    return render(request, 'account.html', {'count': count})

def logout(request):
    messages.info(request, "You are now logged out !")
    auth.logout(request)
    return redirect('/')

def cart(request):
    totalPrice = 0
    totalAmount = 0
    cartItem = Cart.objects.filter()
    count = Cart.objects.all().count()
    for item in cartItem:
        totalPrice = totalPrice + item.price
        totalAmount = totalAmount + item.amount
    data=Cart.objects.all()
    context = {'posts':data, 'totalPrice': totalPrice, 'totalAmount': totalAmount, 'count': count}
    return render(request, 'cart.html', context)

def add(request):
    totalPrice = 0
    totalAmount = 0
    check = 0
    if request.method == 'POST':
        name = request.POST.get('name', False)
        price = request.POST.get('price', False)
        image = request.POST.get('image', False)
        amount = request.POST.get('amount', False)
        new = Cart(name = name, price = int(price) * int(amount), image = image, amount = amount)
        new.save()
        data = Cart.objects.all()
        cartItem = Cart.objects.filter()
        for item in cartItem:
            totalPrice = totalPrice + item.price
            totalAmount = totalAmount + item.amount
        count = Cart.objects.all().count()
        context = {'posts':data, 'totalPrice': totalPrice, 'totalAmount': totalAmount, 'count': count, 'check': check}
        messages.success(request, "Product added to cart !")
    return render(request, 'cart.html', context)

def delete(request, pk):
    new = Cart.objects.get(id=pk)
    new.delete()
    messages.info(request, "Deleted product !")
    return redirect('/cart')

def payment(request):
    data = Cart.objects.all()
    data.delete()
    check = 1
    count = Cart.objects.all().count()
    context = {'count': count, 'check': check}
    messages.success(request, "Your payment was successful !")
    return render(request, 'cart.html', context)
