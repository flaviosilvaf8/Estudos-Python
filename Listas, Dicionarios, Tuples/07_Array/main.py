from array import array #importando módulo do array

letras = ['a', 'b', 'c']
numero_i = [10, 20, 30]
numero_f = [1.2, 2.2, 3.2]

print(letras)
print(numero_i)
print(numero_f)
print()

# usa-se array para grandes listas
letras = array('u', ['a', 'b', 'c']) # u para letras
numero_i = ('i', [10, 20, 30]) # i de int
numero_f = ('f', [1.2, 2.2, 3.2]) # f de float

print(letras)
print(numero_i)
print(numero_f)
print()

