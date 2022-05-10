from django.forms import ModelForm
from .models import Materia
from .models import Material
from .models import Assunto

class MateriaForm(ModelForm):
	class Meta:
		model = Materia
		fields = ['nome']

class AssuntoForm(ModelForm):
	class Meta:
		model = Assunto
		fields = ['titulo', 'materia']

class MaterialForm(ModelForm):
	class Meta:
		model = Material
		fields = ['tipo', 'material', 'assunto']