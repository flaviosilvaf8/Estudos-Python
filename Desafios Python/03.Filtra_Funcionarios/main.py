# Desafio com 'Sets'

'''
Criar um programa que gera 3 listas de acordo com a necessidade logo abaixo:

Lista1 = Funcionarios que tem carro e trabalham a noite
Lista2 = Funcionarios que tem carro e trabalham durante o dia
Lista3 = Funcionarios que não tem carro
'''

funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Paulo', 'João', 'Simão']
turno_dia = ['Ana', 'Marcos', 'Simão']
turno_noite = ['Pedro', 'Paulo', 'João', 'Alice']
tem_carro = ['Marcos', 'Alice', 'João', 'Simão']

#Lista 1
lista1 = set(tem_carro).intersection(turno_noite)
print(lista1)

#Lista 2
lista2 = set(tem_carro).intersection(turno_dia)
print(lista2)

#Lista 3
lista3 = set(funcionarios).difference(tem_carro)
print(lista3)





