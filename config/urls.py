from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('cidade/', CidadesView.as_view(), name='cidade'),
    path('ocupacao/', OcupacoesView.as_view(), name='ocupacao'),
    path('instituicao/', InstituicoesView.as_view(), name='instituicao'),
    path('areasaber/', AreasSaberView.as_view(), name='areasaber'),
    path('curso/', CursosView.as_view(), name='curso'),
    path('disciplina/', DisciplinasView.as_view(), name='disciplina'),
    path('pessoa/', PessoasView.as_view(), name='pessoa'),
    path('matricula/', MatriculasView.as_view(), name='matricula'),
    path('avaliacaotipo/', AvaliacaoTiposView.as_view(), name='avaliacaotipo'),
    path('avaliacao/', AvaliacoesView.as_view(), name='avaliacao'),
    path('frequencia/', FrequenciasView.as_view(), name='frequencia'),
    path('turno/', TurnosView.as_view(), name='turno'),
]


