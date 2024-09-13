# Dicionarios
    # Utiliza index mo formato de Key e Values
    # Aceita string, integer, float, boolean...
  
#Visualizando Itens, Key e Values


aluno = {
        'nome': 'Ana',
         'Idade': 16, 
         'nota_final': 'A', 
         'aprovacao': True,
         'Materias': [
             'Fisica', 'Matematica', 'Ingles'
             ]
         }

print(aluno.items())
print(aluno.keys())
print(aluno.values())
print(aluno.get('Materias'))