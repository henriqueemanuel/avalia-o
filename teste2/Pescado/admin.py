from django.contrib import admin
from .models import informacoes_peixe


class informacoes_peixe_admin(admin.ModelAdmin):
    pass

admin.site.register(informacoes_peixe,informacoes_peixe_admin)
