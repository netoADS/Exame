#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida,
#crie uma nova lista que contenha apenas os números que são divisíveis por um número fornecido pelo usuário.

print('Escreva uma lista de numeros\n')

lista = [1,2,3,4,5,6,7,8,9,10]
newLista = []
numero = int(input('Insira um numero: '))
for i in lista:
    if numero%i == 0:
        newLista.append(i)

print('os numeros divisiveis pelo numero fornecido pelo usuário são: ', newLista)