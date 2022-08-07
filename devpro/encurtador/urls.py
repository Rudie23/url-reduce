from django.urls import path

from devpro.encurtador import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:slug>', views.redirecturl, name='redirecturl'),
    path('relatorios/', views.relatorio, name='relatorio'),  # Tive que criar uma função nova
    path('relatorios/<slug:slug>', views.relatorios, name='relatorios'),

]
