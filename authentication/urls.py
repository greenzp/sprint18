from django.urls import path
from . import views

urlpatterns = [
  path('user/<int:user_id>', views.user_info, name='user info'),
  path('all', views.all_users, name='all users')
  ]
