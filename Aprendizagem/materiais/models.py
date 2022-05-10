from django.db import models
from datetime import datetime

class Materia(models.Model):
	nome = models.CharField(max_length=100)
	data_criacao = models.DateTimeField(auto_now_add=True, blank=True)

	def __str__(self):
		return self.nome

class Assunto(models.Model):
	materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
	titulo = models.CharField(max_length=100)
	data_criacao = models.DateTimeField(auto_now_add=True, blank=True)

	def __str__(self):
		return self.titulo

class Material(models.Model):
	tipos = [('pdf', 'PDF'),
			 ('img', 'IMG'),
			 ('txt', 'TXT'),
			]
	assunto = models.ForeignKey(Assunto, on_delete=models.CASCADE)
	tipo = models.CharField(max_length=20, choices=tipos)
	material = models.FileField(upload_to='')
	data_criacao = models.DateTimeField(auto_now_add=True, blank=True)