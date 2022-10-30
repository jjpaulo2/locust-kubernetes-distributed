from rest_framework.serializers import ModelSerializer

from api.models import (
    Author,
    Book,
    Consumer,
    Order
)


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ('pk', 'name', 'birth_date')


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ('pk', 'title', 'subtitle', 'author')


class ConsumerSerializer(ModelSerializer):
    class Meta:
        model = Consumer
        fields = ('pk', 'name', 'birth_date', 'document_cpf')


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ('pk', 'consumer', 'book', 'price')
