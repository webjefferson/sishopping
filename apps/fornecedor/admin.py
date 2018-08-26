from django.contrib import admin

from apps.fornecedor.models import Fornecedor, Telefone

admin.site.register(Telefone)
admin.site.register(Fornecedor)
