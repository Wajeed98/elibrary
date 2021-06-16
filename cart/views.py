from django.shortcuts import redirect, render
from books.models import BookTrending,BookDiscount,BookInfo,BookFavourite, Category
from order.models import Order
from .models import Cart,CartDiscount,CartTrend,User
from accounts.models import UserInfo
# Create your views here.

def add_to_cart(request,id):
    book=BookInfo.objects.get(id=id)
    uid=request.session.get('_auth_user_id')
    user=User.objects.get(id=uid)
    cr=Cart()
    cr.user=user
    cr.book=book
    #cr.quantity=request.POST.get('quantity')
    cr.save()
    return redirect('/')

def add_to_cart_trend(request,id):
    book=BookTrending.objects.get(id=id)
    uid=request.session.get('_auth_user_id')
    user=User.objects.get(id=uid)
    crt=CartTrend()
    crt.user=user
    crt.book=book
    #crt.quantity=request.POST.get('quantity')
    crt.save()
    return redirect('/')

def add_to_cart_dis(request,id):
    book=BookDiscount.objects.get(id=id)
    uid=request.session.get('_auth_user_id')
    user=User.objects.get(id=uid)
    crd=CartDiscount() 
    crd.user=user
    crd.book=book
    #crd.quantity=request.POST.get('quantity')
    crd.save()
    return redirect('/')

def cart_list(request):
    uid=request.session.get('uid')
    u=UserInfo.objects.get(id=uid)
    balance=u.balance
    uid=request.session.get('_auth_user_id')
    cr=Cart.objects.all()
    crt=CartTrend.objects.all()
    crd=CartDiscount.objects.all()
    o=Order.objects.all()
    cl=Category.objects.all()
    bl=BookInfo.objects.all()
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
        context={'cr':cr,'crt':crt,'crd':crd,'cl':cl,'bl':bl,'clist':clist,'clist_dis':clist_dis,
        'clist_trend':clist_trend,'cart_value':cart_value,'order_value':order_value,'bal':bal,'balance':balance}
        return render(request,'cart_list.html',context)
    
def delete_cart(request,id):
    cr_id=Cart.objects.get(id=id)
    cr_id.delete()
    return redirect('/cart--list')

def delete_cart_trend(request,id):
    crt_id=CartTrend.objects.get(id=id)
    crt_id.delete()
    return redirect('/cart--list')

def delete_cart_dis(request,id):
    crd_id=CartDiscount.objects.get(id=id)
    crd_id.delete()
    return redirect('/cart--list')