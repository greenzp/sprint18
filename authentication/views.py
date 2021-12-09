from datetime import timedelta

from django.shortcuts import render
from django.db.models import F
# Create your views here.
from author.models import Author
from book.models import Book
from order.models import Order
from authentication.models import CustomUser

TEMPLATE_DIRS = 'os.path.join(BASE_DIR,"templates")'


def user_info(request, user_id):
    user = CustomUser.objects.filter(id=user_id)
    orders = Order.objects.filter(user=user_id)
    return render(request, 'user_info.html', context={'user': user, 'orders': orders})


def all_users(request):
    users = CustomUser.get_all()
    orders = Order.objects.filter(plated_end_at__gt=F('created_at') + timedelta(days=3, minutes=1)).order_by('user')
    print(orders)
    return render(request, 'all_users.html', context={'users': users, 'orders': orders})
