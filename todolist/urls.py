from django.urls import path, include
from rest_framework import routers
from todolist import views



router = routers.DefaultRouter()
router.register(r'GET/api/todolist', views.GETTareaView, basename='gettarea')
router.register(r'POST/api/todolist', views.POSTTareaView, basename='posttarea')
router.register(r'PATCH/api/todolist', views.PATCHTareaView, basename='patchtarea')
router.register(r'DELETE/api/todolist', views.DELETETareaView, basename='deletetarea')

router.register(r'GET/api/Usuarios', views.GETUsuarioView, basename='getusuario')
router.register(r'POST/api/Usuarios', views.POSTUsuarioView, basename='postusuario')
router.register(r'PATCH/api/Usuarios', views.PATCHUsuarioView, basename='patchusuario')
router.register(r'DELETE/api/Usuarios', views.DELETEUsuarioView, basename='deleteusuario')

router.register(r'GET/api/Usuarios', views.UsuarioViewSet, basename='getusuariotarea')

urlpatterns = [
    path('', include(router.urls)),
]