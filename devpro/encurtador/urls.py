from django.urls import path

from devpro.encurtador import views

urlpatterns = [
    path('<slug:slug>', views.redirect1),
]