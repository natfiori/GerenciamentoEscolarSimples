from django.db import models
from cadastros.models import Matricula


class Nota(models.Model):
    codMatricula = models.ForeignKey(Matricula, on_delete=models.PROTECT)
    avaliacao = models.CharField(max_length=30)
    nota = models.IntegerField()
    data = models.DateField()

    def __str__(self):
        return '{}'.format(self.codMatricula) + " | " + '{}'.format(self.avaliacao)


class Frequencia(models.Model):
    presente = 'P'
    ausente = 'F'
    frequencia_opcoes = {
        presente: 'P',
        ausente: 'F'
    }
    frequencia_escolha = (
        (presente, frequencia_opcoes[presente]),
        (ausente, frequencia_opcoes[ausente])
    )
    codMatricula = models.ForeignKey(Matricula, on_delete=models.PROTECT)
    data = models.DateField()
    status = models.CharField(max_length=2, choices=frequencia_escolha)

    def __str__(self):
        return '{}'.format(self.codMatricula) + " | " + '{}'.format(self.data)
