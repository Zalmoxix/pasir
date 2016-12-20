from django.conf.urls import url
import views
from .views import *
from .forms import *

urlpatterns = [
    url(r'^$', index.as_view()),
    url(r'^imagenes/$', VistaImagenes.as_view(), name='imagenes'),
    url(r'^versiones/$', VistaVersiones.as_view(), name='versiones'),
    url(r'^grupos/$', VistaGrupos.as_view(), name='grupos'),
    url(r'^scripts/$', VistaScripts.as_view(), name='scripts'),
    url(r'^equipos/$', VistaEquipos.as_view(), name='equipos'),
    url(r'^actequipo/$', VistaActequipo.as_view(), name='actequipo'),
    url(r'^logs/$', VistaLogs.as_view(), name='logs'),
#    url(r'^autoversion/$', views.AutoVersion, name='autoversion'),
    ]
