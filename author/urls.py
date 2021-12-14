from django.urls import path
from . import views
from author.views import *

urlpatterns = [
  path('author/<int:author_id>', views.author_info, name='author info'),
  path('add/', AuthorCreateView.as_view(), name='add author'),
  path('edit/<int:author_id>', views.edit_author, name='edit author'),
  path('delete/<int:author_id>', views.delete_author, name='delete author')
  ]