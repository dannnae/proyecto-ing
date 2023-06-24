from django.contrib import admin
from .models import Usuario, MetodoPago, Solicitud, TipoSoli

admin.site.register(Usuario)
admin.site.register(Solicitud)
admin.site.register(MetodoPago)
admin.site.register(TipoSoli)

