# Desafio if, else, elif

'''
Criar um programa que dependendo da temperatura (Em Celsius) do steak ele retornará o ponto de cozimento em portugues. O usuario deverá fornecer a temperatura.

Temperaturas - Cozimento
48ºC - Selada
54ºC - Ao ponto para mal
60ºC - Ao ponto
65ºC - Ao ponto para bem
71ºC - Bem passada
'''

temperatura = int(input('Olá, qual é a temperatura da carne: '))

if temperatura in range (48, 53):
    print("O ponto da carne é selada!")
elif temperatura in range (54, 59):
    print('O ponto da carne é ao ponto para mal!')
elif temperatura in range (60, 64):
    print('O ponto da carne é ao ponto!')
elif temperatura in range (65, 70):
    print('O ponto da carne é ao ponto para bem!')
elif temperatura >= 71:
    print('O ponto da carne é bem passado!')
elif temperatura < 48:
    print('Asse um pouco mais por gentileza!')



