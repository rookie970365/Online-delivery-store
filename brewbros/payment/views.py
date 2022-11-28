import braintree
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from orders.models import Order


def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        order.paid = True
        order.save()
        return render(request, 'payment/done.html', {'order': order})
    else:
        return render(request, 'payment/process.html', {'order': order})


def payment_done(request):
    return render(request, 'payment/done.html')



# создаем экземпляр шлюза Braintree BraintreeGateway()на основе конфигурации, определенной в настройках проекта
# gateway = braintree.BraintreeGateway(settings.BRAINTREE_CONF)


# def payment_process(request):
#     # получаем текущий order_id сеанса, который был сохранен в сеансе с помощью order_create
#     order_id = request.session.get('order_id')
#     # извлекаем Order объект по заданному order_id
#     order = get_object_or_404(Order, id=order_id)
#     total_cost = order.get_total_cost()
#     if request.method == 'POST':
#         # извлекаем Одноразовый номер токена для оплаты для создания новой транзакции
#         nonce = request.POST.get('payment_method_nonce', None)
#         # создание и отправка транзакции
#         result = gateway.transaction.sale({
#             'amount': f'{total_cost:.2f}',
#             'payment_method_nonce': nonce,
#             'options': {
#                 'submit_for_settlement': True
#             }
#         })
#         if result.is_success:
#             # помечаем заказ как оплаченный
#             order.paid = True
#             # сохраняем уникальный идентификатор транзакции
#             order.braintree_id = result.transaction.id
#             order.save()
#             return redirect('payment:done')
#         else:
#             return redirect('payment:canceled')
#     else:
#         # если GET, генерируем токен клиента
#         client_token = gateway.client_token.generate()
#         return render(request,
#                       'payment/process.html',
#                       {'order': order,
#                        'client_token': client_token})
