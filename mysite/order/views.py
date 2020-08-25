from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from order.models import ShopCart, ShopCartForm, OrderForm, OrderDetail, Order
from product.models import Category


@login_required(login_url='/login')
def index(request):
    categoryList = Category.objects.all()
    current_user = request.user
    orders = Order.objects.all().filter(user_id=current_user.id)

    context = {
        'page': 'orders',
        'orders': orders,
        'categoryList': categoryList,
    }
    return render(request, 'order_list.html', context)


@login_required(login_url='/login')
def shop_cart_add(request,proid):
    url = request.META.get('HTTP_REFERER')
    form = ShopCartForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            current_user = request.user
            quantity = form.cleaned_data['quantity']
            try:
                q1 = ShopCart.objects.get(user_id=current_user.id, product_id=proid)
            except ShopCart.DoesNotExist:
                q1 = None
            if q1 != None:
                q1.quantity = q1.quantity + quantity
                q1.save()
            else:
                data = ShopCart(user_id=current_user.id, product_id=proid, quantity=quantity)
                data.save()
            request.session['cart_items'] = ShopCart.objects.filter(user_id=current_user.id).count()
            messages.success(request, "Product added to cart")
            return HttpResponseRedirect(url)
    # return HttpResponseRedirect(reverse('product', args=[proid]))
    return HttpResponseRedirect("/product/" + str(proid) + "/")


@login_required(login_url='/login')
def shop_cart_delete(request, id):
    url = request.META.get('HTTP_REFERER')
    ShopCart.objects.filter(id=id).delete()
    messages.success(request, "Product deleted from cart..")
    return HttpResponseRedirect(url)


@login_required(login_url='/login')
def shop_cart_list(request):
    categoryList = Category.objects.all()
    current_user = request.user
    shopcart = ShopCart.objects.all().filter(user_id=current_user.id)
    carttotal = 0
    for rs in shopcart:
        carttotal += rs.quantity * rs.product.price

    context = {'page': 'cart',
               'shopcart': shopcart,
               'carttotal': carttotal,
               'categoryList': categoryList,
               }
    return render(request, 'shop_cart_list.html', context)


@login_required(login_url='/login')
def order_detail(request, id):
    categoryList = Category.objects.all()
    order = Order.objects.get(pk=id)
    items = OrderDetail.objects.all().filter(order=id)
    context = {
        'page': 'detail',
        'order': order,
        'items': items,
        'categoryList': categoryList
    }
    return render(request, 'order_detail.html', context)


@login_required(login_url='/login')
def shop_cart_checkout(request):
    categoryList = Category.objects.all()
    current_user = request.user
    shopcart = ShopCart.objects.all().filter(user_id=current_user.id)
    carttotal = 0
    for rs in shopcart:
        carttotal += rs.quantity * rs.product.price

    form = OrderForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            # Credit Card information section if bank accept payment then order==true
            data = Order()
            data.name = form.cleaned_data['name']
            data.surname = form.cleaned_data['surname']
            data.address = form.cleaned_data['address']
            data.city = form.cleaned_data['city']
            data.phone = form.cleaned_data['phone']
            data.to = form.cleaned_data['name']
            data.user_id = current_user.id
            data.total = carttotal
            data.save()
            for rs in shopcart:
                detail = OrderDetail()
                detail.order_id = data.id
                detail.product_id = rs.product.id
                detail.user_id = current_user.id
                detail.quantity = rs.quantity
                detail.price = rs.product.price
                detail.total = rs.amount
                detail.save()
            ShopCart.objects.filter(user_id=current_user.id).delete()
            request.session['cart_items'] = 0
            messages.success(request, "Order has been completed ")
            return HttpResponseRedirect("/order")

    context = {'page': 'checkout',
               'shopcart': shopcart,
               'carttotal': carttotal,
               'categoryList': categoryList,

               }
    return render(request, 'shop_cart_checkout.html', context)
