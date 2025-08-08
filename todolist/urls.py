from django.urls import path, include
from rest_framework import routers
from todolist import views

from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


router = routers.DefaultRouter()
router.register(r'GET/api/todolist', views.GETTareaView, basename='gettarea')
router.register(r'POST/api/todolist', views.POSTTareaView, basename='posttarea')
router.register(r'PATCH/api/todolist', views.PATCHTareaView, basename='patchtarea')
router.register(r'DELETE/api/todolist', views.DELETETareaView, basename='deletetarea')

urlpatterns = [
    path('', include(router.urls)),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]