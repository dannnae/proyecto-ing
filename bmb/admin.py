from django.contrib import admin
from .models import Bicicleta, Despacho, Usuario, MetodoPago, Solicitud, TipoSoli

admin.site.register(Usuario)
admin.site.register(Solicitud)
admin.site.register(MetodoPago)
admin.site.register(TipoSoli)
admin.site.register(Despacho)
admin.site.register(Bicicleta)




