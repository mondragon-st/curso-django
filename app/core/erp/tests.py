from django.test import TestCase
import config.wsgi
from core.erp.models import Type

# Listarr
#query = Type.objects.all()
#print(query)

# Insercion
#Tipo = Type(name='Diligenciero').save()
#Tipo.name = 'Programador'
#Tipo.save()

#Editar
#Tipo = Type.objects.get(id=3)
#Tipo.name = 'Develop'
#Tipo.save()

# Eliminar
#Tipo = Type.objects.get(pk=4)
#Tipo.delete()

#Tipo = Type.objects.filter(name__icontains='Dir')#Contengan '' excluyendo mayus o minus
#Tipo = Type.objects.filter(name__startswith='D').query#Empiecen con ''
#print(Tipo)

