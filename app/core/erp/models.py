from django.db import models
from django.utils.timezone import now
from datetime import datetime


# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        db_table = 'Tipo'
        ordering = ['-id']


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        db_table = 'Categoria'
        ordering = ['-id']


class Employee(models.Model):
    category = models.ManyToManyField(Category)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, verbose_name='Nombres', null=False, blank=False)
    dni = models.CharField(max_length=10, unique=True, verbose_name='DNI')
    date_joined = models.DateField(default=datetime.now(), verbose_name='Fecha de registro')
    date_creation = models.DateTimeField(auto_now=True, verbose_name='Fecha de creación')
    date_updated = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de actualización')
    age = models.PositiveIntegerField(default=0, null=False, blank=False)
    salary = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    state = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', null=True, blank=True)
    c_vitae = models.ImageField(upload_to='c_vitae/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'empleado'
        ordering = ['-id']