from django.db import models

# Create your models here.


class UrlRedirect(models.Model):
    destino = models.URLField(max_length=512)
    slug = models.SlugField(max_length=128, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'UrlRedirect para {self.destino}'


class UrlLog(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    origem = models.URLField(max_length=512, null=True, blank=True)  # o null eu coloco para dizer se é opcional
    user_agent = models.CharField(max_length=512, null=True, blank=True)  # De qual dispositivo a pessoa está
    # acessando esse link
    host = models.CharField(max_length=512, null=True, blank=True)  # nome do dompinio ondea pessoa cliclou
    ip = models.GenericIPAddressField(null=True, blank=True)
    url_redirect = models.ForeignKey(UrlRedirect, models.DO_NOTHING, related_name='logs')  # qual o nome da
    # propriedade que vai referenciar todos os logs conectados a UrlRedirect. Isso vai criar automaticamente uma
    # propriedade 'logs' no UrlRedirect pelo qual eu vou conseguir listar todos os logs conectados ao UrlRedirect

    def __str__(self):
        return f'UrlRedirect para {self.url_redirect}'
