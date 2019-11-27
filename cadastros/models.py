from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Professor(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11)
    titulacao = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Disciplina(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Matricula(models.Model):
    codAluno = models.ForeignKey(Aluno, on_delete=models.PROTECT)
    codDisciplina = models.ForeignKey(Disciplina, on_delete=models.PROTECT)
    dataIn = models.DateField()
    dataFi = models.DateField()

    def __str__(self):
        return '{}'.format(self.codAluno) + " | " + '{}'.format(self.codDisciplina)


class HistoricoDisciplina(models.Model):
    codProfessor = models.ForeignKey(Professor, on_delete=models.PROTECT)
    codDisciplina = models.ForeignKey(Disciplina, on_delete=models.PROTECT)
    dataIn = models.DateField()
    dataFi = models.DateField()

    def __str__(self):
        return '{}'.format(self.codProfessor) + " | " + '{}'.format(self.codDisciplina)



