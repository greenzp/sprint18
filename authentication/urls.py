from django.urls import path
from . import views


urlpatterns = [
    path('', views.CustomUserView.as_view()),
    path('<int:pk>/', views.CustomUserDetail.as_view()),
    path('<int:user_id>/order/', views.user_order_list),
    path('<int:user_id>/order/<int:order_id>/', views.user_order_detail),
    ]
