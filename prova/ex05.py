#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, imprima a lista ordenada em ordem crescente.

print('digite uma lista de números\n')

lista = []
for i in range(5):
    lista.append(int(input('Digite um numero: ')))
    lista.sort()

print('Lista em ordem crescente: ', lista)