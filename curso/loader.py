import json

from curso.models import Curso, Disciplina

Curso.objects.all().delete()
Disciplina.objects.all().delete()

print("bruh")

with open('curso/json/curso.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

curso_info = data['courseDetail']
curso = Curso(
    nome=curso_info['courseName'],
    codigo=curso_info['courseCode'],
    apresentacao=curso_info['presentation'],
    objetivos=curso_info['objectives'],
    competencias=curso_info['competences'],
    ects=curso_info['courseECTS'],
    duracao_semestres=curso_info['semesters'],
    departamento=curso_info['departement'],
    contacto_direcao=curso_info['directionContact'],
    email_direcao=curso_info['directionEmail'],
    contacto_secretaria=curso_info['courseSecretariatContact'],
    email_secretaria=curso_info['courseSecretariatEmail']
)
curso.save()
print('import curso OK!')

for info in data['courseFlatPlan']:
    disciplina = Disciplina(
        nome=info['curricularUnitName'],
        ano=info['curricularYear'],
        semestre=info['semester'],
        ects=info['ects'],
        codigo_leitura=info['curricularIUnitReadableCode']
    )
    disciplina.save()

print("Dados importados com sucesso")
