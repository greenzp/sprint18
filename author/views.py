from django.shortcuts import render

# Create your views here.
from author.models import Author
from book.models import Book
from order.models import Order

TEMPLATE_DIRS = 'os.path.join(BASE_DIR,"templates")'


def author_info(request, author_id):
    author = Author.objects.filter(id=author_id)
    # books = Author.objects.filter()
    # print(books)
    return render(request, 'author_info.html', context={'authors': author})
