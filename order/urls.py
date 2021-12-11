from django.urls import path
from . import views

urlpatterns = [
    path('<int:order_id>/', views.order_info, name='order_info'),
    path('', views.FilteredListView.as_view(), name='all_orders'),
    path('form/', views.add_order, name='order_form'),
    path('delete/<int:order_id>/', views.order_delete, name='order_delete'),
    path('edit/<int:order_id>/', views.order_edit, name='order_edit'),
]
