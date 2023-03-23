#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, encontre e imprima o segundo número mais alto na lista.

print('digite uma lista de numeros\n')

lista = []
for i in range(5):
    lista.append(int(input('Digite um numero: ')))
    lista.sort()
print(lista[-2])