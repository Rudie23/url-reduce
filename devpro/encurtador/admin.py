from django.contrib import admin

# Register your models here.
from devpro.encurtador.models import UrlRedirect


@admin.register(UrlRedirect)
class UrlRedirectAdmin(admin.ModelAdmin):
    list_display = ('destino', 'slug', 'created_at', 'updated_at')
