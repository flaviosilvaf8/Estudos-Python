# Desafios com funções 

'''
Criar um programa que calcula a quantidade de tinta necessaria para pintar uma parede. O usuario deverá fornecer as seguintes informações: Rendimento, altura e largura.
O programa deve mostrar na tela a mensagem 'Você necessita de x latas de tinta'
'''

rendimento = int(input('Qual é o rendimento da lata: '))
altura = int(input('Qual é a altura da parede: '))
largura = int(input('Qual é a largura da parede: '))

def calc_lata():
    return (altura * largura) / rendimento

numero_latas = calc_lata()
print(f'Você precisará de {numero_latas} latas de tinta')



