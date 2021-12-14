from rest_framework import serializers
from book.models import Book


class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('name', 'description', 'count', 'authors')
