# from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Competencia, Materia, Docente, Bloom
from .serializers import CompetenciaSerializer, MateriaSerializer, DocenteSerializer, BloomSerializer

@permission_classes([IsAuthenticated])
class CombinedViewSet(viewsets.ViewSet):
    def list(self, request):
        
        self.base_name = 'combined'
        
        # Consulta todos os objetos dos modelos e serializa-os
        materias = Materia.objects.all()
        docentes = Docente.objects.all()
        blooms = Bloom.objects.all()
        
        materias_serializer = MateriaSerializer(materias, many=True)
        docentes_serializer = DocenteSerializer(docentes, many=True)
        blooms_serializer = BloomSerializer(blooms, many=True)

        # Combine as respostas em um único dicionário JSON
        combined_data = {
            'materias': materias_serializer.data,
            'docentes': docentes_serializer.data,
            'blooms': blooms_serializer.data,
        }

        return Response(combined_data)

# @api_view(['GET'])
@permission_classes([IsAuthenticated])
class PesquisarMateria(viewsets.ViewSet):
    def list(self, request):
        # Obtém os parâmetros de pesquisa do URL
        materia_id = request.query_params.get('id')
        materia_codigo = request.query_params.get('codigo')

        self.base_name = 'pesquisar-materia'
        
        # Inicializa a variável de resultado
        resultado = None

        # Realiza a pesquisa com base no ID ou no código
        if materia_id:
            try:
                resultado = Materia.objects.get(id=materia_id)
            except Materia.DoesNotExist:
                return Response({'mensagem': 'Matéria não encontrada'}, status=status.HTTP_404_NOT_FOUND)
        elif materia_codigo:
            try:
                resultado = Materia.objects.get(codigo=materia_codigo)
            except Materia.DoesNotExist:
                return Response({'mensagem': 'Matéria não encontrada'}, status=status.HTTP_404_NOT_FOUND)

        if resultado:
            # Serializa o resultado e retorna como resposta
            serializer = MateriaSerializer(resultado)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'mensagem': 'Nenhum parâmetro de pesquisa fornecido'}, status=status.HTTP_400_BAD_REQUEST)

@permission_classes([IsAuthenticated])
class InserirBlooms(viewsets.ViewSet):
    serializer_class = BloomSerializer
    basename='inserir_blooms'
    
    def create(self, request):
        data = request.data

        # Se o corpo da requisição contém uma lista de objetos Bloom
        if isinstance(data, list):
            serializer = self.serializer_class(data=data, many=True)
        else:
            serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes([IsAuthenticated])
class ListarCompetencias(viewsets.ReadOnlyModelViewSet):
    basename='listar_competencias'
    queryset = Competencia.objects.all().order_by('id')
    serializer_class = CompetenciaSerializer

@permission_classes([IsAuthenticated])
class ListarDocentes(viewsets.ReadOnlyModelViewSet):
    basename='listar_docentes'
    queryset = Docente.objects.all().order_by('nome')
    serializer_class = DocenteSerializer
    
# @api_view(['PUT'])
@permission_classes([IsAuthenticated])
class AtualizarTermoAceito(viewsets.ViewSet):
    def update(self, request):
        self.basename = 'atualizar_termo_aceito'
        print("chegou")
        try:
            docente_id = request.query_params.get('id')
            docente = Docente.objects.get(id=docente_id)
        except Docente.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'PUT':
            serializer = DocenteSerializer(docente, data={'termo_aceito': True}, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)