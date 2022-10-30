from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.swagger import schema_view
from api.views import (
    AuthorViewSet,
    BookViewSet,
    ConsumerViewSet,
    OrderViewSet
)


router = DefaultRouter()
router.register('authors', AuthorViewSet)
router.register('books', BookViewSet)
router.register('consumer', ConsumerViewSet)
router.register('orders', OrderViewSet)


urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]
