from django.contrib import admin
from .models import Aluno, Professor, Disciplina, Matricula, HistoricoDisciplina

admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(Disciplina)
admin.site.register(Matricula)
admin.site.register(HistoricoDisciplina)


