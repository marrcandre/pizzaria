from django.db import models

class Tipo(models.Model):
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao

class Pizza(models.Model):
    name = models.CharField(max_length=30)
    tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT, related_name='pizzas')

    def __str__(self):
        return f'{self.name} ({self.tipo})'