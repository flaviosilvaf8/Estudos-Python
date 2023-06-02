cores = ['azul', 'verde', 'amarelo', 'vermelho']
cor_cliente = input('Informe a cor desejada: ')


while True:
    if cor_cliente.lower() in cores:
        print('Cor em estoque')
        break
    else:
        print('Não temos essa cor em estoque')
        cor_cliente = input('Digite outra cor:')
        continue
        
    