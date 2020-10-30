from django.contrib import admin
from .models import informacoes_pescaria

# Register your models here.
class informacoes_pescaria_admin(admin.ModelAdmin):
    pass


admin.site.register(informacoes_pescaria, informacoes_pescaria_admin)