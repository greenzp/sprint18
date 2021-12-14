from rest_framework import serializers
from author.models import Author


class AuthorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class AuthorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name', 'surname', 'patronymic')