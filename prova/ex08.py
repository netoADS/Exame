#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, imprima apenas os números que são maiores do que 10.
print('Escreva uma lista de numeros\n')
lista = []
for i in range(5):
    numero = int(input('digite um numero: '))
    if numero > 10:
        lista.append(numero)
print('os numeros maiores que 10 são: ',lista)