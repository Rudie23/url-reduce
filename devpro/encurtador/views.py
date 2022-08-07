from django.shortcuts import render, redirect

# Create your views here.
from devpro.encurtador.models import UrlRedirect


def home(request):
    return render(request, 'base/home.html')


def relatorio(request):
    return render(request, 'base/relatorio.html')


def relatorios(request, slug):
    url_redirect = UrlRedirect.objects.get(slug=slug)  # Eu quero que o slug do meu UrlRedirect seja igual ao do
    # parâmetro que está sendo passado na função
    # Para criar uma url completa, e incluindo o esquema e o domínio. Ela recebe como parametro
    url_reduzida = request.build_absolute_uri(f'/{slug}')
    ctx = {'reduce': url_redirect,
           'url_reduzida': url_reduzida}
    return render(request, 'base/relatorio.html', ctx)


def redirecturl(request, slug):
    url_redirect = UrlRedirect.objects.get(slug=slug)  # Eu quero que o slug do meu UrlRedirect seja igual ao do
    # parâmetro que está sendo passado na função
    return redirect(url_redirect.destino)
