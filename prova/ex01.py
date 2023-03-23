#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, imprima apenas os números pares da lista.

print('Digite uma sequencia de numeros\n')

list = []
newList = []

for i in range(10):
    list.append(int(input('Insira um numero: ')))

for x in list:
    if x%2 != 1:
        newList.append(x)

print('Os numeros pares são: '+newList)