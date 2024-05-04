from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CombinedViewSet, PesquisarMateria, InserirBlooms, ListarCompetencias, ListarDocentes, AtualizarTermoAceito

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register('api', CombinedViewSet, basename='combined')
router.register(r'pesquisar-materia', PesquisarMateria, basename='pesquisar-materia')
router.register(r'inserir-blooms', InserirBlooms, basename='inserir_blooms')
router.register(r'listar-competencias', ListarCompetencias, basename='listar_competencias')
router.register(r'listar-docentes', ListarDocentes, basename='listar_docentes')
# router.register(r'atualizar-termo', AtualizarTermoAceito, basename='atualizar_termo_aceito')

urlpatterns = [
    path('api/', include(router.urls)),
    
    path(r'atualizar-termo/', AtualizarTermoAceito.as_view({'put': 'update'}), name="atualizar_termo_aceito"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]