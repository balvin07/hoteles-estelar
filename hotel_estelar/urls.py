from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from encuesta import views  # Asegúrate de importar las vistas necesarias

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.formulario_encuesta, name='formulario'),  # Define tus rutas
    path('gracias/', views.gracias, name='gracias'),
    # Otras rutas de tu aplicación
]

# Solo en modo de desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
