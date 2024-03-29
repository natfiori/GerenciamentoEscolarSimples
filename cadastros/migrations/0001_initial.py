# Generated by Django 2.2.6 on 2019-11-27 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataIn', models.DateField()),
                ('dataFi', models.DateField()),
                ('codAluno', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.Aluno')),
                ('codDisciplina', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.Disciplina')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('endereco', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=11)),
                ('titulacao', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avaliacao', models.CharField(max_length=30)),
                ('nota', models.IntegerField()),
                ('data', models.DateField()),
                ('codMatricula', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.Matricula')),
            ],
        ),
        migrations.CreateModel(
            name='Frequencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('status', models.CharField(choices=[('P', 'P'), ('F', 'F')], max_length=2)),
                ('codMatricula', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.Matricula')),
            ],
        ),
    ]
