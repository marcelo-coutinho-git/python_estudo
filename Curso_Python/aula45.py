# Python Object-Oriented Programming
    #Classes
        # Utilizadas para criar Objetos (instances)
        # Objetos sao partes dentro de uma Class (instancias)
        # Classes dao utilizadas para agrupar dados e funcoes, podendo reutiliza-las
    #======
        # Class: Frutas
        # Objects: Abacate, Banana....

from datetime import datetime
    # criar a classe  
class Funcionarios:
    def __init__(self, nome, sobrenome, ano_nasc): # Self = objeto.argumento
        self.nome      = nome
        self.sobrenome = sobrenome
        self.ano_nasc = ano_nasc
        
    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome
    
    def idade_funcionario(self):
         ano_atual = datetime.now().year
         self.ano_nasc = int(ano_atual - self.ano_nasc)
         return self.ano_nasc

# criar o Objeto   
usuario1 = Funcionarios('Bernardo', 'Coutinho', 2023)
usuario2 = Funcionarios('Marcelo', 'Coutinho', 1986)

    # Print
print(Funcionarios.nome_completo(usuario2))
print(Funcionarios.idade_funcionario(usuario2))



