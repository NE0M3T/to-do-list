from django.urls import path, include
from rest_framework import routers
from todolist import views

router = routers.DefaultRouter()
router.register(r'GET/api/todolist', views.GETTareaView, basename='gettarea')
router.register(r'POST/api/todolist', views.POSTTareaView, basename='posttarea')
router.register(r'PATCH/api/todolist', views.PATCHTareaView, basename='patchtarea')
router.register(r'DELETE/api/todolist', views.DELETETareaView, basename='deletetarea')

urlpatterns = [
    path('', include(router.urls)),
]