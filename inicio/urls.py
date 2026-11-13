from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profesores/', views.profesores_list, name='profesores_list'),
    path('profesores/editar/<int:id>/', views.editar_profesor, name='editar_profesor'),
    path('profesores/eliminar/<int:id>/', views.eliminar_profesor, name='eliminar_profesor'),
]
