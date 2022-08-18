from tabnanny import verbose
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Professor(models.Model):
    nome = models.CharField(max_length=124)
    idade = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "professores"

class Avaliacao(models.Model):
    descricao = models.TextField(max_length=600)
    nota = models.IntegerField(
        default=1, 
        validators=[MaxValueValidator(100), MinValueValidator(0)]
    )
    data = models.DateField(auto_now=True)
    professor_refe = models.ForeignKey(Professor, on_delete=models.CASCADE, default=None)
    class Meta:
        verbose_name_plural = "Avaliações"     