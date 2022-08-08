from django.db.models import Count
from django.db.models.functions import TruncDate
from django.shortcuts import render, redirect

# Create your views here.
from devpro.encurtador.models import UrlRedirect, UrlLog


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
           'url_reduzida': url_reduzida,

           }
    return render(request, 'base/relatorio.html', ctx)


# https://docs.djangoproject.com/en/4.1/ref/request-response/
def redirecturl(request, slug):
    url_redirect = UrlRedirect.objects.get(slug=slug)  # Eu quero que o slug do meu UrlRedirect seja igual ao do
    # parâmetro que está sendo passado na função
    UrlLog.objects.create(
        origem=request.META.get('HTTP_REFERER'),
        user_agent=request.META.get('HTTP_USER_AGENT'),
        host=request.META.get('HTTP_HOST'),
        ip=request.META.get('REMOTE_ADDR'),
        url_redirect=url_redirect
    )
    return redirect(url_redirect.destino)
