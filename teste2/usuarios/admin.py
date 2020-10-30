from django.contrib import admin
from .models import cadastro_usuario

# Register your models here.
class cadastro_usuario_admin(admin.ModelAdmin):
    pass


admin.site.register(cadastro_usuario, cadastro_usuario_admin)