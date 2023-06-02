valor = input('Qual o valor da compra:')
compra_confirmada = True
dados_compra = f'Compra no valor de {valor} e entrega confirmada'

for enviar in range(3):
    if compra_confirmada:
        print(dados_compra)
        print("Detalhes enviado para o seu email")
        break
else:
    print('Falha na compra')        