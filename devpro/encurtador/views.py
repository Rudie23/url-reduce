from django.shortcuts import render, redirect

# Create your views here.
from devpro.encurtador.models import UrlRedirect


def redirect1(request, slug):
    url_redirect = UrlRedirect.objects.get(slug=slug)  # Eu quero que o slug do meu UrlRedirect seja igual ao do
    # parâmetro que está sendo passado na função

    return redirect(url_redirect.destino)
