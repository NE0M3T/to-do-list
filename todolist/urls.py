from django.urls import path, include
from rest_framework import routers
from todolist import views

router = routers.DefaultRouter()
router.register(r'', views.TareaView)

urlpatterns = [
    path('todolist/', include(router.urls)),
]