from rest_framework.serializers import HyperlinkedModelSerializer

from api.models import (
    Author,
    Book,
    Consumer,
    Order
)


class AuthorSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ('name', 'birth_date')


class BookSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'subtitle', 'author')


class ConsumerSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Consumer
        fields = ('name', 'birth_date', 'document_cpf')


class OrderSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('consumer', 'book', 'price')
