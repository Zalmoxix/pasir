from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.conf import settings
from django.db.models.signals import post_save
from smart_selects.db_fields import ChainedForeignKey 
from django import forms


class Imagen(models.Model):
	nombre_imagen = models.CharField('Nombre', max_length=50, default='imagen')
	descripcion_imagen = models.CharField('Descripcion', max_length=300)
	fecha_imagen = models.DateField('Ultima modificacion', default=datetime.date.today)
	ip_golden_client = models.GenericIPAddressField()
	def __str__(self):
		return self.nombre_imagen


class Version(models.Model):
	descripcion_version = models.CharField('Descripcion', max_length=300, default='Version inicial')
	numero_version = models.CharField('Version', max_length=20, default='1.0')
	fecha_version = models.DateField('Ultima modificacion', default=datetime.date.today)
	golden_client = models.CharField('Golden_Client', max_length=20, default='ip_equipo_golden')
	imagen = models.ForeignKey(Imagen)
	def __str__(self):
		return self.imagen.nombre_imagen+' '+self.numero_version


class Grupo(models.Model):
	fecha_grupo = models.DateField('Ultima modificacion', default=datetime.date.today)
	nombre_grupo = models.CharField('Nombre', max_length=50, default='grupo')
	imagen = models.ForeignKey(Imagen)
	version = ChainedForeignKey(
		Version, 
		chained_field="imagen",
		chained_model_field="imagen", 
		show_all=False, 
		auto_choose=True
	)
	def __str__(self):
		return self.nombre_grupo

class Script(models.Model):
	nombre_script = models.CharField('Nombre', max_length=50, default='script')
	ruta = models.FilePathField(path="/var/lib/systemimager/scripts", match=".master", recursive=False)
	fecha_script = models.DateField('Ultima modificacion', default=datetime.date.today)
	grupo = models.ForeignKey(Grupo)
	def __str__(self):
		return self.nombre_script

class Equipo(models.Model):
	disponible = models.BooleanField(default=True)
	ultimasinc = models.DateField('Fecha ultima sincronizacion', default=datetime.date.today)
	dominio = models.CharField('Nombre dominio', max_length=50, default='dominio')
	ip_equipo = models.GenericIPAddressField()
	grupo = models.ForeignKey(Grupo)
	script_equipo = models.CharField('Nombre Script', max_length=50, default='script')
	def __str__(self):
		return str(self.dominio)



class Log(models.Model):
	nombre_log = models.CharField('Nombre', max_length=50, default='log')
	fecha_log = models.DateField('Fecha creacion', default=datetime.date.today)
	ruta = models.FilePathField(path="/home/alberto/pasir-master/logs", match=".log", recursive=False)
	equipo = models.ForeignKey(Equipo)
	def __str__(self):
		return self.nombre_log
	

