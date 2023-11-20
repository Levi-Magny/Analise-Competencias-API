# Generated by Django 4.2.4 on 2023-10-03 03:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('codigo', models.CharField(max_length=10)),
                ('competencias', models.ManyToManyField(to='stuprofile.competencia')),
            ],
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('materias', models.ManyToManyField(to='stuprofile.materia')),
            ],
        ),
        migrations.CreateModel(
            name='Bloom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i_index', models.IntegerField()),
                ('j_index', models.IntegerField()),
                ('competencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stuprofile.competencia')),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stuprofile.docente')),
            ],
        ),
    ]
