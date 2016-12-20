from django.views.generic import ListView
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404, render, redirect, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import DetailView
from django.views.generic.base import View, TemplateResponseMixin, ContextMixin
from django.views.generic.edit import FormMixin, ProcessFormView
from django.template import RequestContext
import subprocess
import datetime
import time
from django.dispatch import receiver
from django.db.models.signals import post_save



class index(CreateView):
	template_name = 'systemimager/index.html'
	form_class = ScriptForm
	context_object_name = 'form'
	success_url = '/systemimager/'

class VistaImagenes(CreateView):
	template_name = 'systemimager/imagenes.html'
	form_class = ImagenForm
	context_object_name = 'form'
	success_url = '/imagenes/'
	

	
#	subprocess.check_output(string, shell=True) 
'''
	def add_context(request):
		if request.method == "POST":
			imagen = Imagen.objects.get(nombre_imagen=request.POST['nombre_imagen'])
			request.session['nombre_imagen'] = imagen.nombre_imagen
			return HttpResponseRedirect('/autoversion/')
		else: 
			return HttpResponseRedirect('/systemimager/')
	
'''	
@receiver(post_save, sender=Imagen)
def AutoVersion(sender, **kwargs):	
	
	versionauto = Version(descripcion_version='Version automatica', numero_version='1.0', fecha_version=datetime.date.today(), golden_client=kwargs['instance'].ip_golden_client, imagen=kwargs['instance'])
	versionauto.save()
	
	string = "ssh root@"+str(kwargs['instance'].ip_golden_client)+' \"'+"si_prepareclient --server 192.168.3.1 --no-uyok --yes"+'\"'+" >> /home/alberto/pasir-master/logs/"+str(kwargs['instance'].ip_golden_client)+".log"
	subprocess.call(string, shell=True)
	return HttpResponseRedirect('/systemimager/')
'''
'''

@receiver(post_save, sender=Imagen)
def GetImage(sender, **kwargs):	
	time.sleep(30)
	string2 = "sudo si_getimage --golden-client "+str(kwargs['instance'].ip_golden_client)+" --image "+str(kwargs['instance'].nombre_imagen)+" --quiet --ip-assignment DHCP >> /home/alberto/pasir-master/logs/"+str(kwargs['instance'].nombre_imagen)+".log"
	subprocess.call(string2, shell=True)
	
	
class VistaVersiones(CreateView):
	template_name = 'systemimager/versiones.html'
	form_class = VersionForm
	context_object_name = 'form'
	success_url = '/versiones/'

@receiver(post_save, sender=Version)
def CheckVersion(sender, **kwargs):	
	string = 'sudo mkdir -p /var/lib/systemimager/overrides/'+str(kwargs['instance'].imagen)+'_'+str(kwargs['instance'].numero_version)
	subprocess.check_output(string, shell=True)
	return HttpResponseRedirect('/systemimager/')


class VistaGrupos(CreateView):
	template_name = 'systemimager/grupos.html'
	form_class = GrupoForm
	context_object_name = 'form'
	success_url = '/grupos/'
	
@receiver(post_save, sender=Grupo)
def CheckGrupo(sender, **kwargs):	
	string = 'echo Se ha creado un grupo con exito >> /home/alberto/prueba.txt'
	subprocess.check_output(string, shell=True)
	return HttpResponseRedirect('/systemimager/')	

class VistaScripts(CreateView):
	template_name = 'systemimager/scripts.html'
	form_class = ScriptForm
	context_object_name = 'form'
	success_url = '/scripts/'
	
@receiver(post_save, sender=Script)
def CheckScript(sender, **kwargs):	
	string = 'echo Se ha creado un script con exito >> /home/alberto/prueba.txt'
	subprocess.check_output(string, shell=True)
	return HttpResponseRedirect('/systemimager/')

class VistaEquipos(CreateView):
	template_name = 'systemimager/equipos.html'
	form_class = EquipoForm
	context_object_name = 'form'
	success_url = '/equipos/'
	
class VistaActequipo(FormView):
	template_name = 'systemimager/actequipo.html'
	form_class = ActequipoForm
	context_object_name = 'form'
	success_url = '/actequipo/'
	
@receiver(post_save, sender=Equipo)
def CheckEquipo(sender, **kwargs):	
	string = 'sudo si_addclients --hosts '+str(kwargs['instance'].ip_equipo)+' --domainname '+str(kwargs['instance'].dominio)+' --script '+str(kwargs['instance'].script_equipo)+' --interactive NO >> /home/alberto/pasir-master/logs/'+str(kwargs['instance'].ip_equipo)+'.log'
	subprocess.check_output(string, shell=True)
	return HttpResponseRedirect('/systemimager/')	

class VistaLogs(CreateView):
	template_name = 'systemimager/logs.html'
	form_class = LogForm
	context_object_name = 'form'
	success_url = '/logs/'
	
@receiver(post_save, sender=Log)
def CheckLog(sender, **kwargs):	
	string = 'echo Se ha creado un log con exito >> /home/alberto/prueba.txt'
	subprocess.check_output(string, shell=True)
	return HttpResponseRedirect('/systemimager/')
	
	
	
'''	
	def form_valid(self, form):
		imagen = form['Imagen'].save()
		version = form['Version'].save()
		return redirect(self.get_success_url())		
'''
'''
def scriptView(request):
    # Handle file upload
    if request.method == 'POST':
        form = ScriptForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Script(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect('/')
    else:
        form = ScriptForm() # A empty, unbound form

    # Load documents for the list page
    scripts = Script.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'systemimager/index.html',
        {'scriptss': scripts, 'form': form},
        context_instance=RequestContext(request)
    )
'''
'''		
class index(CreateView):
	template_name = 'templated-ion/index.html'
	form_class = GrupoForm
	context_object_name = 'form'
	success_url = '/systemimager/'
'''	

'''
class MultiFormMixin(ContextMixin):

    form_classes = {} 
    prefixes = {}
    success_urls = {}
    grouped_forms = {}
    
    initial = {}
    prefix = None
    success_url = None
     
    def get_form_classes(self):
        return self.form_classes
     
    def get_forms(self, form_classes, form_names=None, bind_all=False):
        return dict([(key, self._create_form(key, klass, (form_names and key in form_names) or bind_all)) \
            for key, klass in form_classes.items()])
    
    def get_form_kwargs(self, form_name, bind_form=False):
        kwargs = {}
        kwargs.update({'initial':self.get_initial(form_name)})
        kwargs.update({'prefix':self.get_prefix(form_name)})
        
        if bind_form:
            kwargs.update(self._bind_form_data())

        return kwargs
    
    def forms_valid(self, forms, form_name):
        form_valid_method = '%s_form_valid' % form_name
        if hasattr(self, form_valid_method):
            return getattr(self, form_valid_method)(forms[form_name])
        else:
            return HttpResponseRedirect(self.get_success_url(form_name))
     
    def forms_invalid(self, forms):
        return self.render_to_response(self.get_context_data(forms=forms))
    
    def get_initial(self, form_name):
        initial_method = 'get_%s_initial' % form_name
        if hasattr(self, initial_method):
            return getattr(self, initial_method)()
        else:
            return self.initial.copy()
        
    def get_prefix(self, form_name):
        return self.prefixes.get(form_name, self.prefix)
        
    def get_success_url(self, form_name=None):
        return self.success_urls.get(form_name, self.success_url)
    
    def _create_form(self, form_name, klass, bind_form):
        form_kwargs = self.get_form_kwargs(form_name, bind_form)
        form_create_method = 'create_%s_form' % form_name
        if hasattr(self, form_create_method):
            form = getattr(self, form_create_method)(**form_kwargs)
        else:
            form = klass(**form_kwargs)
        return form
           
    def _bind_form_data(self):
        if self.request.method in ('POST', 'PUT'):
            return{'data': self.request.POST,
                   'files': self.request.FILES,}
        return {}


class ProcessMultipleFormsView(ProcessFormView):
    
    def get(self, request, *args, **kwargs):
        form_classes = self.get_form_classes()
        forms = self.get_forms(form_classes)
        return self.render_to_response(self.get_context_data(forms=forms))
     
    def post(self, request, *args, **kwargs):
        form_classes = self.get_form_classes()
        form_name = request.POST.get('action')
        if self._individual_exists(form_name):
            return self._process_individual_form(form_name, form_classes)
        elif self._group_exists(form_name):
            return self._process_grouped_forms(form_name, form_classes)
        else:
            return self._process_all_forms(form_classes)
        
    def _individual_exists(self, form_name):
        return form_name in self.form_classes
    
    def _group_exists(self, group_name):
        return group_name in self.grouped_forms
              
    def _process_individual_form(self, form_name, form_classes):
        forms = self.get_forms(form_classes, (form_name,))
        form = forms.get(form_name)
        if not form:
            return HttpResponseForbidden()
        elif form.is_valid():
            return self.forms_valid(forms, form_name)
        else:
            return self.forms_invalid(forms)
        
    def _process_grouped_forms(self, group_name, form_classes):
        form_names = self.grouped_forms[group_name]
        forms = self.get_forms(form_classes, form_names)
        if all([forms.get(form_name).is_valid() for form_name in form_names.values()]):
            return self.forms_valid(forms)
        else:
            return self.forms_invalid(forms)
        
    def _process_all_forms(self, form_classes):
        forms = self.get_forms(form_classes, None, True)
        if all([form.is_valid() for form in forms.values()]):
            return self.forms_valid(forms)
        else:
            return self.forms_invalid(forms)
 
 
class BaseMultipleFormsView(MultiFormMixin, ProcessMultipleFormsView):
    """
    A base view for displaying several forms.
    """
 
class MultiFormsView(TemplateResponseMixin, BaseMultipleFormsView):
    """
    A view for displaying several forms, and rendering a template response.
    """
    
    
class IndexView(MultiFormsView):
	template_name = 'templated-ion/index.html'
	form_classes = {'imagen': ImagenForm,
					'version': VersionForm,
					'grupo': GrupoForm,
					'script': ScriptForm,
					'equipo': EquipoForm,
					'log': LogForm}
	success_url = '/systemimager/'
    
	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		context.update({"some_context_value": 'blah blah blah',
						"some_other_context_value": 'blah'})
		return context

	def imagen_form_valid(self, form):
		imagen = form.save(self.request)
		return form.imagen(self.request, imagen, redirect_url=self.get_success_url())

	def version_form_valid(self, form):
		version = form.save(self.request)
		return form.version(self.request, version, self.get_success_url())
		
	def grupo_form_valid(self, form):
		grupo = form.save(self.request)
		return form.grupo(self.request, grupo, self.get_success_url())
		
	def script_form_valid(self, form):
		script = form.save(self.request)
		return form.script(self.request, script, self.get_success_url())
		
	def equipo_form_valid(self, form):
		equipo = form.save(self.request)
		return form.equipo(self.request, equipo, self.get_success_url())
		
	def log_form_valid(self, form):
		log = form.save(self.request)
		return form.log(self.request, log, self.get_success_url())
        
'''
