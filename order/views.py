from django.shortcuts import render,redirect
from cart.models import CartDiscount,CartTrend,Cart,User
from accounts.models import UserInfo
from books.models import BookDiscount,BookTrending,BookInfo,Category
from .models import Order
# Create your views here.

def get_order_list(request):
    uidi=request.session.get('uid')
    u=UserInfo.objects.get(id=uidi)
    balance=u.balance
    uid=request.session.get('_auth_user_id')
    cr=Cart.objects.all()
    crt=CartTrend.objects.all()
    crd=CartDiscount.objects.all()
    o=Order.objects.all()
    ord_list=Order.objects.filter(user=uid)
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
    context={'cr':cr,'crt':crt,'crd':crd,'cl':cl,'bl':bl,'clist':clist,'clist_dis':clist_dis,'ord_list':ord_list,
        'clist_trend':clist_trend,'cart_value':cart_value,'order_value':order_value,'balance':balance}
    return render(request,'order_list.html',context)

def delete_order(request,id):
    or_id=Order.objects.get(id=id)
    or_id.delete()
    return redirect('/ord-list')
