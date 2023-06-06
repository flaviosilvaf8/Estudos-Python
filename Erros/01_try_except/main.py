# Erros
    # Excelente para teste
    # Não realiza o 'Stop' no programa
    # Mensagens customizadas quando encontra um erro

try:
    letras = ['a', 'b', 'c']
    print(letras[3])
except IndexError:
    print('Index não existe') # Se ele tentar oque esta dentro do Try e encontrar um index error, imprima a mensagem
