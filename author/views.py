from django.shortcuts import render, redirect

# Create your views here.
from author.models import Author
from book.models import Book
from order.models import Order
from .forms import AuthorForm


from rest_framework import generics
from author.serializers import AuthorDetailSerializer,AuthorListSerializer


TEMPLATE_DIRS = 'os.path.join(BASE_DIR,"templates")'


class AuthorCreateView(generics.CreateAPIView):
    serializer_class = AuthorDetailSerializer


class AuthorsListView(generics.ListAPIView):
    serializer_class = AuthorListSerializer
    queryset = Author.objects.all()










def author_info(request, author_id):
    author = Author.objects.filter(id=author_id)
    # books = Author.objects.filter()
    # print(books)
    return render(request, 'author_info.html', context={'authors': author})


def add_author(request):
    if request.method == 'GET':
        form = AuthorForm()
        return render(request, 'author_form.html', context={'form': form})
    if request.method == 'POST':
        form = AuthorForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('main')


def edit_author(request, author_id):
    if request.method == 'GET':
        author = Author.objects.get(pk=author_id)
        form = AuthorForm(instance=author)
        return render(request, 'author_form.html', context={'form': form})
    if request.method == "POST":
        author = Author.objects.get(pk=author_id)
        form = AuthorForm(request.POST, instance=author)
    if form.is_valid():
        form.save()
    return redirect('author info', author_id=author_id)


def delete_author(request, author_id):
    author = Author.objects.get(pk=author_id)
    author.delete()
    return redirect('main')
