# Generated by Django 4.2.4 on 2024-04-25 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuprofile', '0002_remove_docente_materias_remove_materia_competencias_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='docente',
            name='termo_aceito',
            field=models.BooleanField(default=False),
        ),
    ]
