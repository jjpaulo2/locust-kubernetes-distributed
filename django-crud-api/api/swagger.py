from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Books Store - Swagger UI",
      default_version='v1',
      description="Django CRUD API example for Locust Test",
      contact=openapi.Contact(email="jjpaulo2@protonmail.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
