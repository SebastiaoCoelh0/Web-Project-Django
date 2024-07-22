from django import forms

from .models import Curso, Disciplina, Projeto, LinguagemProgramacao, Docente


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'


class DisciplinaForm(forms.ModelForm):
    cursos = forms.ModelMultipleChoiceField(
        queryset=Curso.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    docentes = forms.ModelMultipleChoiceField(
        queryset=Docente.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    projeto = forms.ModelChoiceField(
        queryset=Projeto.objects.all(),
        required=False
    )

    class Meta:
        model = Disciplina
        fields = '__all__'


class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'


class LinguagemProgramacaoForm(forms.ModelForm):
    class Meta:
        model = LinguagemProgramacao
        fields = '__all__'


class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = '__all__'
