#-*- encoding: utf-8 -*-
from django import forms
from django.contrib import admin
from django.forms import ModelForm
from .models import *
from forms import *
from django.forms import inlineformset_factory
from clever_selects.form_fields import ChainedChoiceField
from clever_selects.forms import ChainedChoicesForm
from multiform import MultiModelForm
from codemirror2.widgets import CodeMirrorEditor

'''
class GrupoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(GrupoForm, self).__init__(*args, **kwargs)
        if self.instance.version:
            self.fields['imagen'].queryset = self.version.objects.filter(
                                                imagen=self.instance.imagen)

'''

'''      
class MultiForm(MultiModelForm):
	base_fields = {}
	form_classes = {
	'Imagen': ImagenForm,
	'Version': VersionForm,
	'Grupo': GrupoForm,
	'Script': ScriptForm,
	'Equipo': EquipoForm,
	'Log': LogForm,
	}
'''



class ImagenForm(ModelForm):
    class Meta:
        model = Imagen
        fields = '__all__'
        
class VersionForm(ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

class GrupoForm(ModelForm):
    class Meta:
        model = Grupo
        fields = '__all__'

class ScriptForm(ModelForm):
	class Meta:
		model = Script
		fields = '__all__' 
		widgets = {
			'text': CodeMirrorEditor(options={'lineNumbers': True, 'mode': "shell", 'matchBrackets': True})}


class EquipoForm(ModelForm):
    class Meta:
        model = Equipo
        fields = '__all__'
        
class LogForm(ModelForm):
    class Meta:
        model = Log
        fields = '__all__'

class MultiForm(MultiModelForm):
	base_fields = {}
	base_forms = [
		('Imagen', ImagenForm),
		('Version', VersionForm),
		]

class ActequipoForm(ModelForm):
    class Meta:
        model = Equipo
        fields = '__all__'
