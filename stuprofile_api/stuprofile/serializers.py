from rest_framework import serializers
from .models import Competencia, Materia, Docente, Bloom

class CompetenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competencia
        fields = '__all__'

class MateriaSerializer(serializers.ModelSerializer):
    competencias = CompetenciaSerializer(many=True, read_only=True)

    class Meta:
        model = Materia
        fields = '__all__'

class DocenteSerializer(serializers.ModelSerializer):
    materias = MateriaSerializer(many=True, read_only=True)

    class Meta:
        model = Docente
        fields = '__all__'

class BloomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bloom
        fields = '__all__'
