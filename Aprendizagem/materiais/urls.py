from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='materias'),
	path('/<int:id_materia>', views.materia, name='materia'),
	path('/<int:id_materia>/<int:id_assunto>', views.assunto, name='assunto'),
	path('/nova_materia', views.nova_materia, name='nova_materia'),
	path('/novo_assunto', views.novo_assunto, name='novo_assunto'),
	path('/novo_material', views.novo_material, name='novo_material'),
	path('/nova_materia_save', views.nova_materia_save, name='nova_materia_save'),
	path('/novo_assunto_save', views.novo_assunto_save, name='novo_assunto_save'),
	path('/novo_material_save', views.novo_material_save, name='novo_material_save'),

]