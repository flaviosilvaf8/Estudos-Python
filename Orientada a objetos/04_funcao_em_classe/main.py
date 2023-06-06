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
    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento

    # Função que irá retornar nome e sobrenome do funcionario
    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome  
    
# Objeto
func1 = Funcionarios('Flavio','Freitas', '28/06/2000')
func2 = Funcionarios('Paulo', 'Pires', '23/09/2003')

#print
print(func1.nome_completo())






    