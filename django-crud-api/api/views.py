from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly
)

from api.serializers import (
    AuthorSerializer,
    BookSerializer,
    ConsumerSerializer,
    OrderSerializer
)
from api.models import (
    Author,
    Book,
    Consumer,
    Order
)


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly,
    )


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly,
    )


class ConsumerViewSet(ModelViewSet):
    queryset = Consumer.objects.all()
    serializer_class = ConsumerSerializer
    permission_classes = (
        IsAuthenticated,
    )


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (
        IsAuthenticated,
    )
