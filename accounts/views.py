from order.models import Order
from cart.models import Cart, CartDiscount, CartTrend,User
from django.shortcuts import render,redirect
from .models import UserInfo,UserInfoForm
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages as msg
from books.models import BookDiscount, BookTrending, Category,BookInfo
# Create your views here.
def update_balance(request):
    uid=request.session.get('uid')
    u=UserInfo.objects.get(id=uid)
    balance=u.balance
    #o=Order.objects.get(id=uid)
    #status=o.status
    #totalBill=o.totalBill
    #if status=='Accepted':
    #    balance = balance - totalBill
    #    return balance
    #else:
    #    return balance
    return balance

def home(request):
    uid=request.session.get('uid')
    #balance=update_balance(request)
    cr=Cart.objects.all()
    crt=CartTrend.objects.all()
    crd=CartDiscount.objects.all()
    o=Order.objects.all()
    clist=Cart.objects.filter(user=uid)
    clist_trend=CartTrend.objects.filter(user=uid)
    clist_dis=CartDiscount.objects.filter(user=uid)
    cart_value=0
    order_value=0
    for i in cr:
        cart_value = cart_value + 1 
    for i in crt:
        cart_value = cart_value + 1 
    for i in crd:
        cart_value = cart_value + 1 
    for i in o:
        order_value = order_value + 1
    cl=Category.objects.all()
    bl=BookInfo.objects.all()
    bt=BookTrending.objects.all()
    bd=BookDiscount.objects.all()
    if request.method=='POST':
        bal=request.POST.get('bal')
        order=Order()
        order.totalBill=bal
        order.user=User.objects.get(id=uid)
        order.save()
        for i in clist:
            i.delete()
        for i in clist_dis:
            i.delete()
        for i in clist_trend:
            i.delete()
        return redirect('/')
    else:
        bal=0
        for i in clist:
            bal = bal + i.book.price * i.quantity
        for i in clist_trend:
            bal = bal + i.book.name.price * i.quantity
        for i in clist_dis:
            bal = bal + i.book.dis_price * i.quantity
    context={'cl':cl,'bl':bl,'bd':bd,'bt':bt,'cart_value':cart_value,'order_value':order_value,
    'clist':clist,'clist_trend':clist_trend,'clist_dis':clist_dis,'bal':bal}
    return render(request,'home.html',context)

def register(request):
    if request.method=='POST':
        f=UserInfoForm(request.POST)
        pass1=request.POST.get('pasa1')
        pass2=request.POST.get('pasa2')
        if pass1!=pass2:
            msg.error(request,'Password Does not Match!')
            context={'form':f,'msg':msg}
            return render(request,'register.html',context)
        else:
            f.save()
            return redirect('/')
    else:
        f=UserInfoForm()
        context={'form':f}
        return render(request,'register.html',context)

def log_in(request):
    if request.method=='POST':
        uname=request.POST.get('uname')
        upass=request.POST.get('upass')
        user=authenticate(request,username=uname,password=upass)
        if user is not None:
            request.session['uid']=user.id
            login(request,user)
            msg.success(request,'Log-In Success')
            return redirect('/')
        else:
            msg.error(request,'Invalid Credentials!')
            return render(request,'login.html')
    else:
        return render(request,'login.html')

def log_out(request):
    logout(request)
    return redirect('/')


def edit_user(request):
    uid=request.session.get('uid')
    balance=update_balance(request)
    cr=Cart.objects.all()
    u=UserInfo.objects.get(id=uid)
    crt=CartTrend.objects.all()
    crd=CartDiscount.objects.all()
    o=Order.objects.all()
    clist=Cart.objects.filter(user=uid)
    clist_trend=CartTrend.objects.filter(user=uid)
    clist_dis=CartDiscount.objects.filter(user=uid)
    cart_value=0
    order_value=0
    for i in cr:
        cart_value = cart_value + 1 
    for i in crt:
        cart_value = cart_value + 1 
    for i in crd:
        cart_value = cart_value + 1 
    for i in o:
        order_value = order_value + 1
    cl=Category.objects.all()
    bl=BookInfo.objects.all()
    bt=BookTrending.objects.all()
    bd=BookDiscount.objects.all()
    if request.method=='POST':
        f=UserInfoForm(request.POST,instance=u)
        pass1=request.GET.get('password1')
        pass2=request.GET.get('password2')
        if pass1!=pass2:
            f=UserInfoForm(instance=u)
            context={'msg':'Error! Both Passwords does not match','form':f,'cl':cl,'bl':bl,'bd':bd,'bt':bt,
            'cart_value':cart_value,'order_value':order_value,'clist':clist,'clist_trend':clist_trend,
            'clist_dis':clist_dis,'balance':balance}
            return render(request,'register.html',context)
        else:
            f.save()
            return redirect('/')
    else:
        f=UserInfoForm(instance=u)
        context={'form':f,'cl':cl,'bl':bl,'bd':bd,'bt':bt,
            'cart_value':cart_value,'order_value':order_value,'clist':clist,'clist_trend':clist_trend,
            'clist_dis':clist_dis,'balance':balance}
        return render(request,'register.html',context)