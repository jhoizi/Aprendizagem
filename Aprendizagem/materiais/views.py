from django.shortcuts import render, redirect
from .models import Materia
from .models import Assunto
from .models import Material
from django.urls import reverse
from .forms import MateriaForm
from .forms import MaterialForm
from .forms import AssuntoForm
from datetime import datetime

def index(response):
	materias = Materia.objects.all()
	url = reverse('materias')
	context = {
		'materias' : materias,
		'url' : url,	
	}
	return render(response ,'materias.html', context)

def materia(response, id_materia):
	materia = Materia.objects.get(id=id_materia)
	assuntos = Assunto.objects.all().filter(materia=materia.id)
	url = reverse('materia', args=[id_materia])
	context = {
		'materia': materia,
		'assuntos': assuntos,
		'url' : url,
		'url_materiais': reverse('materias')
	}

	return render(response, 'materia.html', context)

def assunto(response, id_materia, id_assunto):
	materia = Materia.objects.get(id=id_materia)
	assunto = Assunto.objects.get(id=id_assunto)
	materiais = Material.objects.all().filter(assunto=id_assunto)
	url = reverse('novo_material')
	
	context = {
		'materiais' : materiais,
		'materia' :  materia,
		'assunto' : assunto,
		'url' : url,
	}

	return render(response, 'assunto.html', context)

def nova_materia(response):

	url = reverse('nova_materia')
	context = {
		'form' : MateriaForm,
		'url' : url,
	}

	return render(response, 'nova_materia.html', context)

def novo_assunto(response):
	url = reverse('novo_assunto_save')
	context = {
		'form' : AssuntoForm,
		'url' : url,
	}

	return render(response, 'novo_assunto.html', context)

def novo_material(response):
	url = reverse('novo_material_save')
	context = {
		'form' : MaterialForm,
		'url' : url,
	}

	return render(response, 'novo_material.html', context)

def nova_materia_save(response):
	if(response.method == 'POST'):
		form = MateriaForm(response.POST)

		if(form.is_valid()):
			nome = form.cleaned_data['nome']
			data_criacao = datetime.now()

			materia = Materia(nome=nome, data_criacao=data_criacao)
			materia.save()

	return redirect("index")

def novo_assunto_save(response):
	if(response.method == 'POST'):
		form = AssuntoForm(response.POST)
		
		if(form.is_valid()):
			titulo = form.cleaned_data['titulo']
			materia = form.cleaned_data['materia']
			data_criacao = datetime.now()

			assunto = Assunto(materia=materia, titulo=titulo, data_criacao=data_criacao)
			assunto.save()

	return redirect("index")

def novo_material_save(response):
	if(response.method == 'POST'):
		form = MaterialForm(response.POST, response.FILES)
		
		if(form.is_valid()):

			form.save()

	return redirect("index")