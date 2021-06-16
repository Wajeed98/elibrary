from django.shortcuts import render,redirect
from .models import Category,BookTrending,BookDiscount,BookFavourite,BookInfo
from cart.models import Cart,CartDiscount,CartTrend,User
from order.models import Order
from accounts.models import UserInfo
# Create your views here.
def sort_by_category(request,id):
    uid=request.session.get('uid')
    u=UserInfo.objects.get(id=uid)
    balance=u.balance
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
    
    bal=0
    for i in clist:
        bal = bal + i.book.price * i.quantity
    for i in clist_trend:
        bal = bal + i.book.name.price * i.quantity
    for i in clist_dis:
        bal = bal + i.book.dis_price * i.quantity

    cl=Category.objects.all()
    bl=BookInfo.objects.filter(category=id)
    context={'cl':cl,'bl':bl,'bd':bd,'bt':bt,'cart_value':cart_value,'order_value':order_value,
        'clist':clist,'clist_trend':clist_trend,'clist_dis':clist_dis,'balance':balance,'bal':bal}
    return render(request,'home.html',context)

def book_types(request):
    bt=BookTrending.objects.all()
    bd=BookDiscount.objects.all()
    context={'bd':bd,'bt':bt}
    return render(request,'home.html',context)

def search_books(request):
    uid=request.session.get('uid')
    u=UserInfo.objects.get(id=uid)
    balance=u.balance
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
    
    bal=0
    for i in clist:
        bal = bal + i.book.price * i.quantity
    for i in clist_trend:
        bal = bal + i.book.name.price * i.quantity
    for i in clist_dis:
        bal = bal + i.book.dis_price * i.quantity

    cl=Category.objects.all()
    bl=BookInfo.objects.all()
    if request.method=='POST':
        pname=request.POST.get('srch')
        bl=BookInfo.objects.filter(name__contains=pname)
        context={'cl':cl,'bl':bl,'bd':bd,'bt':bt,'cart_value':cart_value,'order_value':order_value,
        'clist':clist,'clist_trend':clist_trend,'clist_dis':clist_dis,'balance':balance,'bal':bal}
        return render(request,'search.html',context)
    else:
        context={'cl':cl,'bl':bl,'bd':bd,'bt':bt,'cart_value':cart_value,'order_value':order_value,
        'clist':clist,'clist_trend':clist_trend,'clist_dis':clist_dis,'balance':balance,'bal':bal}
        return render(request,'search.html',context)