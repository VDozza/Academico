from django.contrib import admin
from .models import *

class CursoInline(admin.TabularInline):
    model = Curso
    extra = 1

class CursoAreaInline(admin.TabularInline):
    model = CursoArea
    extra = 1

class DisciplinaInline(admin.TabularInline):
    model = Disciplina
    extra = 1

class MatriculaInline(admin.TabularInline):
    model = Matricula
    extra = 1

class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao
    extra = 1

class FrequenciaInline(admin.TabularInline):
    model = Frequencia
    extra = 1

class CursoDisciplinaInline(admin.TabularInline):
    model = CursoDisciplina
    extra = 1

class OcorrenciaInline(admin.TabularInline):
    model = Ocorrencia
    extra = 1

class InstituicaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade')
    search_fields = ('nome',)
    inlines = [CursoInline]

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'instituicao')
    search_fields = ('nome',)
    inlines = [CursoAreaInline, CursoDisciplinaInline]

class AreaSaberAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [DisciplinaInline]

class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ocupacao', 'cidade')
    search_fields = ('nome',)
    inlines = [MatriculaInline, OcorrenciaInline]

class AvaliacaoTipoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [AvaliacaoInline]

class FrequenciaAdmin(admin.ModelAdmin):
    list_display = ('curso', 'disciplina', 'pessoa', 'numero_faltas')
    search_fields = ('curso__nome', 'pessoa__nome')
    inlines = [FrequenciaInline]

class OcorrenciaAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'data', 'curso', 'disciplina', 'pessoa')
    search_fields = ('descricao', 'pessoa__nome')

admin.site.register(Cidade)
admin.site.register(Ocupacao)
admin.site.register(InstituicaoEnsino, InstituicaoAdmin)
admin.site.register(AreaSaber, AreaSaberAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Disciplina)
admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Matricula)
admin.site.register(AvaliacaoTipo, AvaliacaoTipoAdmin)
admin.site.register(Avaliacao)
admin.site.register(Frequencia)
admin.site.register(Turno)
admin.site.register(Turma)
admin.site.register(Ocorrencia, OcorrenciaAdmin)
admin.site.register(CursoDisciplina)
