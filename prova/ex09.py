#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, imprima apenas os números que são menores do que 5.
print('Escreva uma lista de numeros\n')
lista = []
for i in range(5):
    numero = int(input('digite um numero: '))
    if numero < 5:
        lista.append(numero)
print('os numeros menores que 5 são: ',lista)