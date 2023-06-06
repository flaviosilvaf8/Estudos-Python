# Erros
    # Excelente para teste
    # Não realiza o 'Stop' no programa
    # Mensagens customizadas quando encontra um erro
    
  
try:
    valor = int(input('Digite o valor do produto: '))
    print(valor)
except ValueError:
    print('Favor digitar um valor em numero')

print('ola mundo') # mostrara o erro acima caso tenha o erro, e continuara o codigo abaixo    
