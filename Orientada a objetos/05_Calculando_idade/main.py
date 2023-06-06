from datetime import datetime
# Classes
    # Utilizadas para criar Objetos (Instances)
    # Objetos são parte de uma Class (Instancias)
    # Classes são utilizadas para agrupar dados e funções, podendo reutilizar
    # =======
    # Class: Frutas
    # Objects: Abacate, Banana...

# Classe
class Funcionarios: 
    
    # Construtores
    def __init__(self, nome, sobrenome, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento

    # Função que irá retornar nome e sobrenome do funcionario
    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome  
    
    def idade_funcionario(self):
        ano_atual = datetime.now().year
        self.ano_nascimento = int(ano_atual - self.ano_nascimento)
        return self.ano_nascimento
        


# Objeto
func1 = Funcionarios('Flavio','Freitas', 2000)
func2 = Funcionarios('Paulo', 'Pires', 2003)

#print
print(func1.idade_funcionario())






    