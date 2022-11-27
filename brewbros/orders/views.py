from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import notify_order_created


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            notify_order_created.delay(order.id)
            return render(request, 'myauth/me.html', {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'orders/create.html', {'cart': cart, 'form': form})