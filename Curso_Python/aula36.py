# Dicionarios
    # Utiliza index mo formato de Key e Values
    # Aceita string, integer, float, boolean...
    
    
aluno = {'nome': 'Ana', 'Idade': 16, 'nota_final': 'A', 'aprovacao': True}

aluno['nome'] = 'jose' # Primeira forma de atualizar valores dentro do Dicionario
aluno.update({'nome': 'jose', 'nota_final': 'B'}) # Dessa forma podemos atualizar mais de uma Key dentro do dicionario

del aluno['Idade'] # Remover uma Key

print(aluno['nome']) # O dicionario trabalha com Key no Index

print(aluno.get('endereco', 'Não Existe')) # retornar mensagem de erro, caso a Key nao exista
print(aluno)
