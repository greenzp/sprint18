from django.shortcuts import render
from author.models import Author
from book.models import Book
from order.models import Order

# Create your views here.
TEMPLATE_DIRS = 'os.path.join(BASE_DIR,"templates")'


def all_orders(request):
    orders_by_create = Order.objects.order_by('created_at')
    orders_by_plated = Order.objects.order_by('plated_end_at')
    return render(request, 'all_orders.html', context={'orders_create': orders_by_create, 'orders_plated': orders_by_plated})


def order_info(request, order_id):
    order = Order.objects.filter(id=order_id)
    return render(request, 'order_info.html', context={'order': order})