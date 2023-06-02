# map - mapeara todos os index da lista, dicionario, tuples...

def multi (x):
    return x * 2 # função que multiplica um numero x vezes 2

lista = [1, 2, 3, 4]

lista2 = map(multi, lista) # lista2 recebe a multiplicação de cada numero da lista 1 vezes 2

print(list(lista2))

print(list(map(lambda x: x *2, lista))) # Trara o mesmo resultado dos códigos acima, porém em apenas uma linha, pelo uso do LAMBDA.