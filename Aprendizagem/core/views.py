from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse


def index(response):

	url_materias = reverse('materias')
	url_nova_materia = reverse('nova_materia')
	context = {
		'url_materias' : url_materias,
		'url_nova_materia' : url_nova_materia,
	}

	return render(response, 'index.html', context)