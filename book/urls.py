from django.urls import path
from . import views
from .views import BookCreateView
from book.views import *

urlpatterns = [
  path('', views.main_page, name='main'),
  path('books/book/<int:book_id>', views.book_info, name='book info'),
  path('delete/<int:book_id>', views.delete_book, name='delete book'),



  path('add/', BookCreateView.as_view(), name='add book'),
  path('books/all', BookListView.as_view(), name='all books'),
  path('books/all/<int:sort>', views.sort_name_count, name='sort books'),
  path('edit/<int:book_id>', views.edit_book, name='edit book'),
  ]
