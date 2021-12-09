from django.urls import path
from . import views

urlpatterns = [
  path('', views.main_page, name='main'),
  path('books/all', views.all_books, name='all books'),
  path('books/all/<int:sort>', views.sort_name_count, name='sort books'),
  path('books/book/<int:book_id>', views.book_info, name='book info')
  ]
