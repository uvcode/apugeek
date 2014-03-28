from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
	titulo = models.CharField(max_length = 100)
	clase = models.CharField(max_length = 80)

	def __unicode__(self):
		return self.titulo

class Enlace(models.Model):
	titulo = models.CharField(max_length = 130)
	enlace = models.URLField()
	descripcion = models.CharField(max_length = 150)
	comentarios = models.IntegerField(default = 0)
	categoria = models.ForeignKey(Categoria)
	usuario = models.ForeignKey(User)
	timestamp = models.DateTimeField(auto_now_add = True)


	def __unicode__(self):
		return "%s - %s" % (self.titulo, self.enlace)


		
		

# Create your models here.
