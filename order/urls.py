from django.urls import path
from . import views

urlpatterns = [
  path('order/<int:order_id>', views.order_info, name='order info'),
  path('all', views.all_orders, name='all orders')
  ]