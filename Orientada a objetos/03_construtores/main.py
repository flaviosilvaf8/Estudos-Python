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

# Objeto
func1 = Funcionarios('Flavio','Freitas', '28/06/2000')
func2 = Funcionarios('Paulo', 'Pires', '23/09/2003')

#print
print(func1.nome)
print(func2.nome)


# Parametros func1
'''func1.nome = 'João'
func1.sobrenome = 'Almeida'
func1.nome = '12/01/2007'

# Parametros func2
func2.nome = 'Pedro'
func2.sobrenome = 'Silva'
func2.nome = '22/05/2002'
'''



    