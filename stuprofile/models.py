from django.db import models

class Competencia(models.Model):
    descricao = models.CharField(max_length=500)

    def __str__(self):
        return self.descricao

class Materia(models.Model):
    nome = models.CharField(max_length=255)
    codigo = models.CharField(max_length=10)
    docentes = models.ManyToManyField('Docente', related_name='materias')

    def __str__(self):
        return self.nome

class Docente(models.Model):
    nome = models.CharField(max_length=255)
    termo_aceito = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nome

class Bloom(models.Model):
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    competencia = models.ForeignKey(Competencia, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    i_index = models.IntegerField()
    j_index = models.IntegerField()

    def __str__(self):
        return f'Bloom para {self.docente.nome}, {self.materia.nome}'
