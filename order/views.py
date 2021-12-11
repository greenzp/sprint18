from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from order.models import Order
from .forms import OrderForm, OrderFormEdit
from django.http import Http404
from django_tables2 import Table, A, Column
from django_filters import rest_framework as filters
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin


# Create your views here.
TEMPLATE_DIRS = 'os.path.join(BASE_DIR,"templates")'


class OrdersFilter(filters.FilterSet):
    book__name = filters.CharFilter(lookup_expr='icontains')
    user__first_name = filters.CharFilter(lookup_expr='icontains')
    user__last_name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Order
        fields = []


class OrderTable(Table):
    id = Column(linkify=("order_info", [A("pk")]))

    class Meta:
        model = Order
        template_name = "django_tables2/bootstrap.html"
        fields = ('id', 'user', "book", 'created_at', 'plated_end_at', 'end_at')


class FilteredListView(SingleTableMixin, FilterView):
    table_class = OrderTable
    model = Order
    filterset_class = OrdersFilter
    template_name = "all_orders.html"


def order_info(request, order_id):
    try:
        order = Order.objects.get(pk=order_id)
    except Order.DoesNotExist:
        raise Http404
    return render(request, 'order_info.html', context={'order': order})


def add_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.plated_end_at = datetime.now() + timedelta(days=15)
            post.save()
        return redirect('all_orders')
    else:
        form = OrderForm()
    return render(request, 'order_form.html', {'form': form})


def order_delete(request, order_id):
    try:
        order = Order.objects.get(pk=order_id)
        order.delete()
    except Order.DoesNotExist:
        raise Http404
    return redirect('all_orders')


def order_edit(request, order_id):
    try:
        order = Order.objects.get(pk=order_id)
    except Order.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        form = OrderFormEdit(instance=order)
        return render(request, 'order_form.html', context={'form': form})
    if request.method == "POST":
        form = OrderFormEdit(request.POST, instance=order)
    if form.is_valid():
        form.save()
    return redirect('all_orders')
